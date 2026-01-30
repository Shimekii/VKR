import numpy as np
from scipy.linalg import expm
import core.analysisModule as am
from numpy.fft import ifft

class MAP:
    def __init__(self, q=None, lamb=None, d=None, size=None, name=None):
        self.current_time = 0
        self.time_next_event = None
        self.time_next_transition = None
        self.isCreated = False
        if name:
            self.__load_from_file(name)
            self.R = am.compute_stationary_distribution(self.Q)
            self.isCreated = True
        else:
            if len(lamb) and len(d) == len(q):
                self.size = size
                self.Q = q
                if lamb.ndim == 1:
                    self.lambda_ = np.zeros((size, size))
                    for i in range(size):
                        self.lambda_[i][i] = lamb[i]
                else:
                    self.lambda_ = lamb
                self.D = d
                self.R = am.compute_stationary_distribution(self.Q)
                self.isCreated = True
        self.current_state = self.__InitialState()
        self._schedule_next()

    def __load_from_file(self, filename):
        with open(filename, 'r') as file:
            # Считываем размер матрицы
            self.size = int(file.readline().strip())

            # Считываем матрицу Q
            self.Q = np.zeros((self.size, self.size))
            for i in range(self.size):
                line = file.readline().strip()
                if line:  # Проверяем, что строка не пустая
                    self.Q[i] = [float(x) for x in line.split()]

            # Считываем диагональные элементы для матрицы Lambda
            self.lambda_ = np.zeros((self.size, self.size))
            for i in range(self.size):
                line = file.readline().strip()
                if line:  # Проверяем, что строка не пустая
                    self.lambda_[i][i] = float(line)

            # Считываем матрицу D
            self.D = np.zeros((self.size, self.size))
            for i in range(self.size):
                line = file.readline().strip()
                if line:  # Проверяем, что строка не пустая
                    self.D[i] = [float(x) for x in line.split()]

            self.R = np.zeros(self.size)

    def show(self):
        print("Q matrix:")
        print(self.Q)
        print("Lambda matrix:")
        print(self.lambda_)
        print("D matrix:")
        print(self.D)
        print("Стационарные вероятности:", self.R)

    # Экспоненциальное распределение
    def __ExpDist(self, lamb):
        u = np.random.uniform(0.0, 1.0)
        return -np.log(1 - u) / lamb

    # Функция перехода по цепи маркова
    def __Transition(self, current_state):
        r = np.random.uniform(0.0, 1.0)

        total_rate = -self.Q[current_state][current_state]
        probability = 0.0

        for i in range(self.size):
            if i != current_state:
                probability += self.Q[current_state][i] / total_rate
                if r < probability:
                    return i
        return current_state

    # Функция выбора начального состояния
    def __InitialState(self):
        r = np.random.uniform(0.0, 1.0)
        probability = 0.0
        for i in range(self.size):
             probability += self.R[i]
             if r < probability:
                return i
        return 0

    # Фукнция генерации выборки событий
    def simutale(self, total_time=None, total_events=None, events=None):
        with open("log.txt", "w") as file_log, open("events.txt", "w") as file_events:
            current_state = self.__InitialState()
            #file_log.write(f"First state: {current_state}\n")
            #file_log.write(f"{'Time':>15}{'State':>15}\n")
            current_time = 0.0
            count_events = 0
            if total_time is not None:
                # Симуляция по времени
                while current_time < total_time:
                    per = (current_time / total_time) * 100
                    print(f"\rProgress: {per:.2f}%", end="")

                    time_to_next_event = self.__ExpDist(self.lambda_[current_state][current_state]) # время следующего события
                    time_to_next_transition = self.__ExpDist(-self.Q[current_state][current_state]) # время следующего перехода

                    next_event_time = current_time + time_to_next_event
                    next_transition_time = current_time + time_to_next_transition

                    next_time = min(next_event_time, next_transition_time)
                    current_time = next_time

                    while current_time < total_time and current_time < next_transition_time:
                        file_log.write(f"{current_time:>15.6f}{current_state:>15} Event\n")
                        file_events.write(f"{current_time:.6f}\n")
                        if events is not None: events.append(current_time)
                        time_to_next_event = self.__ExpDist(self.lambda_[current_state][current_state])
                        current_time += time_to_next_event

                    if current_time >= next_transition_time:
                        current_time = next_transition_time

                    if current_time < total_time:
                        new_state = self.__Transition(current_state)
                        if self.__DidEventOccur(current_state, new_state):
                            file_log.write(f"{current_time:>15.6f}{current_state:>15} Event\n")
                            file_events.write(f"{current_time:.6f}\n")
                            if events is not None:
                                events.append(current_time)
                        file_log.write(f"{current_time:>15.6f}{new_state:>15} Transition\n")
                        current_state = new_state
            elif total_events is not None:
                # Симуляция по количеству событий
                while count_events < total_events:
                    per = (count_events / total_events) * 100
                    print(f"\rProgress: {per:.2f}%", end="")

                    time_to_next_event = self.__ExpDist(self.lambda_[current_state][current_state])
                    time_to_next_transition = self.__ExpDist(-self.Q[current_state][current_state])

                    next_event_time = current_time + time_to_next_event
                    next_transition_time = current_time + time_to_next_transition

                    next_time = min(next_event_time, next_transition_time)
                    current_time = next_time

                    while count_events < total_events and current_time < next_transition_time:
                        #file_log.write(f"{current_time:>15.6f}{current_state:>15} Event\n")
                        #file_events.write(f"{current_time:.6f}\n")
                        if events is not None: events.append(current_time)
                        count_events += 1
                        time_to_next_event = self.__ExpDist(self.lambda_[current_state][current_state])
                        current_time += time_to_next_event

                    if current_time >= next_transition_time:
                        current_time = next_transition_time

                    if count_events < total_events:
                        new_state = self.__Transition(current_state)
                        if self.__DidEventOccur(current_state, new_state):
                            count_events += 1
                            #file_log.write(f"{current_time:>15.6f}{current_state:>15} Event\n")
                            #file_events.write(f"{current_time:.6f}\n")
                            if events is not None:
                                events.append(current_time)
                        current_state = new_state
                        #file_log.write(f"{current_time:>15.6f}{current_state:>15} Transition\n")

    # Генерация одного события
    def step(self):
        if self.time_next_event <= self.time_next_transition:
            self.current_time = self.time_next_event
            self._schedule_next()
            return ('event', self.current_time)
        else:
            self.current_time = self.time_next_transition
            old_state = self.current_state
            new_state = self.__Transition(old_state)
            self.current_state = new_state
            event_transition = self.__DidEventOccur(old_state, new_state)
            self._schedule_next()
            return ('transition', old_state, new_state, self.current_time, event_transition)
        
    # Обновляем время события и перехода
    def _schedule_next(self):
        self.time_next_event = (
            self.current_time +
            self.__ExpDist(self.lambda_[self.current_state][self.current_state])
        )
        self.time_next_transition = (
            self.current_time +
            self.__ExpDist(-self.Q[self.current_state][self.current_state])
        )

    # Проверяет, произошло ли событие при переходе из from_state в to_state.
    def __DidEventOccur(self, from_state, to_state):
        probability = self.D[from_state][to_state]
        return np.random.random() < probability

    # Возвращается параметры Q, Lambda, D
    def getParams(self):
        return self.Q, self.lambda_, self.D

    # Приводит MAP-поток к интенсивности 1
    def _normalize(self):
        #B = np.multiply(self.Q, self.D)  # Q * D
        temp = np.multiply(self.Q, self.D)  # Q * D
        B = np.add(self.lambda_, temp)  # lambda + (Q * D)
        k = np.dot(self.R, np.dot(B, np.ones(len(self.R))))
        Q = np.divide(self.Q, k)
        Lambda = np.divide(self.lambda_, k)
        return Q, Lambda

    def event_count_distribution(self, n_max, t=1):
        """
        Вычисляет распределение числа событий в MAP-потоке за время t.

        :param t: момент времени
        :param n_max: максимальное число событий (n)
        :return: массив вероятностей P_n(t), n=0..n_max
        """
        m = self.size
        k = n_max + 1
        u_vals = 2 * np.pi * np.arange(k) / k
        H_vals = np.zeros(k, dtype=complex)
        Q, Lambda = self._normalize()
        # Матрица генерации событий: B = Λ ◦ D
        B = Lambda + np.multiply(Q, self.D)
        I = np.eye(m)
        # Начальное распределение — стационарное
        e0 = self.R

        for j, u in enumerate(u_vals):
            A_u = Q + (np.exp(1j * u) - 1) * B
            H_t = expm(t * A_u)
            H_vals[j] = np.dot(e0, H_t @ np.ones(m))

        probs = ifft(H_vals).real
        probs = np.maximum(probs, 0)  # Убираем отрицательные шумы

        # Корректировка порядка: P(0) остается, остальное — в обратном порядке
        probs_corrected = np.empty_like(probs)
        probs_corrected[0] = probs[0]
        probs_corrected[1:n_max + 1] = probs[1:n_max + 1][::-1]

        return probs_corrected[:k]