import numpy as np
from scipy.linalg import expm
import core.analysis.analysis as am
from numpy.fft import ifft

class MAP:
    def __init__(self, q=None, lamb=None, d=None, name=None):
        self.isCreated = False
        if name:
            self.__load_from_file(name)
            self.R = am.compute_stationary_distribution(self.Q)
            self.isCreated = True
        else:
            self.size = len(q)
            if len(lamb) == self.size and len(d) == self.size:
                self.Q = q
                lamb = np.array(lamb)
                if lamb.ndim == 1:
                    self.lambda_ = np.zeros((self.size, self.size))
                    for i in range(self.size):
                        self.lambda_[i][i] = lamb[i]
                else:
                    self.lambda_ = lamb
                self.D = d
                self.R = am.compute_stationary_distribution(self.Q)
                self.isCreated = True
                self.current_time = 0
            else:
                raise ValueError("Размеры матриц не совпадают")
        self.current_state = self.__InitialState()
        self.current_time = 0
        self.time_next_event = self.current_time + self.__ExpDist(self.lambda_[self.current_state][self.current_state])
        self.time_next_transition = self.current_time + self.__ExpDist(-self.Q[self.current_state][self.current_state])

    def __load_from_file(self, filename):
        with open(filename, 'r') as file:
            try:
                # Считываем размер матрицы
                self.size = int(file.readline().strip())
            except Exception:
                raise ValueError("Ошибка чтения размерности.")

            try:
                # Считываем матрицу Q
                self.Q = np.zeros((self.size, self.size))
                for i in range(self.size):
                    line = file.readline().strip()
                    if line:  # Проверяем, что строка не пустая
                        self.Q[i] = [float(x) for x in line.split()]
            except Exception:
                raise ValueError("Ошибка чтения матрицы Q.")
            
            try:
                # Считываем диагональные элементы для матрицы Lambda
                self.lambda_ = np.zeros((self.size, self.size))
                for i in range(self.size):
                    line = file.readline().strip()
                    if line:  # Проверяем, что строка не пустая
                        self.lambda_[i][i] = float(line)
            except Exception:
                raise ValueError("Ошибка чтения интенсивностей.")
            
            try:
                # Считываем матрицу D
                self.D = np.zeros((self.size, self.size))
                for i in range(self.size):
                    line = file.readline().strip()
                    if line:  # Проверяем, что строка не пустая
                        self.D[i] = [float(x) for x in line.split()]
            except Exception:
                raise ValueError("Ошибка чтения матрицы D.")

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

    # Генерация одного события
    def step(self):
        if self.time_next_event <= self.time_next_transition:
            self.current_time = self.time_next_event
            self.time_next_event = self.current_time + self.__ExpDist(self.lambda_[self.current_state][self.current_state])
            return ('event', self.current_time, None)
        else:
            self.current_time = self.time_next_transition
            old_state = self.current_state
            new_state = self.__Transition(old_state)
            self.current_state = new_state
            event_transition = self.__DidEventOccur(old_state, new_state)
            self.time_next_event = self.current_time + self.__ExpDist(self.lambda_[self.current_state][self.current_state])
            self.time_next_transition = self.current_time + self.__ExpDist(-self.Q[self.current_state][self.current_state])
            return ('transition', self.current_time, event_transition)

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