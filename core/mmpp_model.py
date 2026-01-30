import numpy as np

class MMPP:
    def __init__(self, q=None, lamb=None, s=None, name=None):
        if name:
            self.__load_from_file(name)
            self.R = compute_stationary_distribution(self.Q)
        else:
            self.size = s
            self.Q = np.array(q) if q is not None else None
            self.lambda_ = np.diag(lamb) if lamb is not None else None
            self.R = compute_stationary_distribution(self.Q)
            self.timestamps = []

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

            self.R = np.zeros(self.size)

    def show(self):
        print("Q matrix:")
        print(self.Q)
        print("Lambda matrix:")
        print(self.lambda_)
        print("Стационарные вероятности:", self.R)

    def __ExpDist(self, lamb):
        u = np.random.uniform(0.0, 1.0)
        return -np.log(1 - u) / lamb

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

    def __InitialState(self):
        r = np.random.uniform(0.0, 1.0)
        probability = 0.0
        for i in range(self.size):
             probability += self.R[i]
             if r < probability:
                return i
        return 0

    def simutale(self, total_time=None, total_events=None, events=None):
        with open("log.txt", "w") as file_log, open("events.txt", "w") as file_events:
            current_state = self.__InitialState()
            file_log.write(f"First state: {current_state}\n")
            file_log.write(f"{'Time':>15}{'State':>15}\n")
            current_time = 0.0
            count_events = 0
            if total_time is not None:
                # Симуляция по времени
                while current_time < total_time:
                    time_to_next_event = self.__ExpDist(self.lambda_[current_state][current_state])
                    time_to_next_transition = self.__ExpDist(-self.Q[current_state][current_state])

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
                        current_state = self.__Transition(current_state)
                        file_log.write(f"{current_time:>15.6f}{current_state:>15} Transition\n")
            elif total_events is not None:
                # Симуляция по количеству событий
                while count_events < total_events:
                    time_to_next_event = self.__ExpDist(self.lambda_[current_state][current_state])
                    time_to_next_transition = self.__ExpDist(-self.Q[current_state][current_state])

                    next_event_time = current_time + time_to_next_event
                    next_transition_time = current_time + time_to_next_transition

                    next_time = min(next_event_time, next_transition_time)
                    current_time = next_time

                    while count_events < total_events and current_time < next_transition_time:
                        file_log.write(f"{current_time:>15.6f}{current_state:>15} Event\n")
                        file_events.write(f"{current_time:.6f}\n")
                        if events is not None: events.append(current_time)
                        count_events += 1
                        time_to_next_event = self.__ExpDist(self.lambda_[current_state][current_state])
                        current_time += time_to_next_event

                    if current_time >= next_transition_time:
                        current_time = next_transition_time

                    if count_events < total_events:
                        current_state = self.__Transition(current_state)
                        file_log.write(f"{current_time:>15.6f}{current_state:>15} Transition\n")

    def getParams(self):
        return self.Q, self.lambda_

def compute_stationary_distribution(Q):
    n = Q.shape[0]

    # Добавляем нормировочное уравнение
    A = np.vstack((Q.T, np.ones(n)))  # Транспонируем Q и добавляем строку
    b = np.zeros(n + 1)  # Вектор свободных членов
    b[-1] = 1  # Нормировочное уравнение

    R = np.linalg.lstsq(A, b, rcond=None)[0]
    return R
    #print(self.R.sum())