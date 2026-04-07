import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

def analysis(data):
    try:
        intervals = np.diff(data)               # длины интервалов
        average_interval = np.mean(intervals)   # средняя длина интервалов
        intensivnost = average_interval ** -1   # интенсивность
        variance = Variance(intervals)
        #variance = np.var(intervals)            # дисперсия
        sigma = np.sqrt(variance)               # среднеквадратичное отклонение
        variation = sigma / average_interval    # коэффициент вариации

        inter_1 = intervals[:-1]
        inter_2 = intervals[1:]

        corr = np.corrcoef(inter_1, inter_2)[0, 1]

        skew_val = skew(intervals, bias=False)
        kurt_val = kurtosis(intervals, bias=False)
        characteristics = (average_interval, variance, variation, corr, skew_val, kurt_val)
        return characteristics
    except Exception as e:
        raise ValueError(e)

def generateRandomParameters(size, type: str, rQ = 10, rLamb = 10):
    Q = np.zeros((size, size))
    Lambda = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            Q[i][j] = np.random.uniform(0, rQ)
            Q[i][i] = 0
    diag = np.sum(Q, axis=1)
    for i in range(size):
        Q[i][i] = -diag[i]
    del (diag)
    for i in range(size):
        Lambda[i][i] = np.random.uniform(0, rLamb)
    if type == 'mmpp':
        return Q, Lambda
    elif type == 'map':
        D = generate_matrix(size)
        return Q, Lambda, D
    else:
        raise ValueError("Такого потока нет")

def getRBE(Q, Lambda, D1, R):
    return np.dot(R, np.dot(D1, np.ones(len(R))))


def characteristics(Q, Lambda, D=None, write=False, name='stat'):
    if D is None:
        D0,D1 = getD0D1(Q, Lambda)
    else:
        D0,D1 = getD0D1(Q, Lambda, D)
    R = compute_stationary_distribution(Q)

    k = np.dot(R, np.dot(D1, np.ones(len(R))))
    mean = k ** -1

    BQ = np.linalg.inv(-D0) # (B-Q)^-1
    E = np.ones(len(R))     # единичный вектор

    # Дисперсия
    temp1 = np.dot(2 * k, R)  # (2 * k) * R
    temp2 = np.dot(temp1, BQ)  # temp1 * (B-Q)^-1
    temp3 = np.dot(temp2, E) - 1  # temp2 * E - 1
    var = temp3 / (k ** 2)

    # Корреляция
    cTemp1 = np.dot((k ** -1), R)  # k^-1 * R
    cTemp2 = np.dot(cTemp1, BQ)  # cTemp1 * (B-Q)^-1
    cTemp3 = np.dot(cTemp2, D1)  # cTemp2 * B
    cTemp4 = np.dot(cTemp3, BQ)  # cTemp3 * (B-Q)^-1
    cTemp5 = np.dot(cTemp4, E) - (k ** -2)  # cTemp4 * E - k^-2
    corr = cTemp5 / var
    #print(k)
    CV = np.sqrt(var) / mean

    M1 = mean
    M2 = var + mean**2
    M3 = 6 * (R @ BQ @ BQ @ E) / k
    M4 = 24 * (R @ BQ @ BQ @ BQ @ E) / k

    mu2 = M2 - M1**2
    mu3 = M3 - 3 * M1 * M2 + 2 * M1**3
    mu4 = M4 - 4 * M1 * M3 + 6 * M1**2 * M2 - 3 * M1**4

    # коэффициент асимметрии
    skewness = mu3 / (var**1.5)

    # Коэффициент эксцесса
    kurtosis = mu4 / (var**2) - 3

    #print('Коэф. асимм. = ', skewness.round(4))
    #print('Коэф. эксцесса = ', kurtosis.round(4))

    if write == True:
        with open(f'{name}.csv', 'a') as file:
            file.write(f"{corr:>5.6f},{CV:6f},{skewness:6f},{kurtosis:6f}\n")
    else:
        """print(f"\nСреднее теоретическое: {mean: 6f}")
        print(f"Теоретическая дисперсия: {var: 6f}")
        print(f"Теоретический коэф. вариации: {CV: 6f}")
        print(f"Теоретическая корреляция: {corr: 6f}")"""
        return mean, var, CV.round(4), corr.round(4), skewness.round(4), kurtosis.round(4)

def Variance(array):
    mean = array.sum()/len(array)
    var = 0
    for i in array:
        var += (i - mean) ** 2
    return var/len(array)


def generate_matrix(n):
    matrix = np.random.rand(n, n)
    np.fill_diagonal(matrix, 0)
    return matrix

def getD0D1(Q, Lambda, D=None):
    if D is None:
        D0 = np.subtract(Q, Lambda) # Q - lambda
        D1 = Lambda
    else:
        B = np.multiply(Q, D)       # Q * D
        D1 = np.add(Lambda, B)      # lambda + (Q * D)
        D0 = np.subtract(Q, D1)     # Q - D1
        assert np.allclose(D0 + D1, Q)
    return D0, D1

def compute_stationary_distribution(Q):
    n = Q.shape[0]

    # Добавляем нормировочное уравнение
    A = np.vstack((Q.T, np.ones(n)))  # Транспонируем Q и добавляем строку
    b = np.zeros(n + 1)  # Вектор свободных членов
    b[-1] = 1  # Нормировочное уравнение

    R = np.linalg.lstsq(A, b, rcond=None)[0]
    return R
    #print(self.R.sum())

# def drawDensity(events, step=0.01):
#     intervals = [np.diff(event) for event in events]
    
#     maxNum = [max(x) for x in intervals]
#     bin_list = [np.arange(0, Max + step, step) for Max in maxNum]
    
#     colorsLine = ['lightcoral', 'olivedrab', 'teal', 'fuchsia']
#     labels = ['Основной поток', 'Поток 1 0.0098', 'Поток 2 0.0258', 'Поток 4 0.0255']
    
#     plt.figure(figsize=(12, 6))

#     for idx, (interval, bins) in enumerate(zip(intervals, bin_list)):
#         N = len(interval)  # общее число интервалов
        
#         # Считаем частоты в бинах
#         counts, bin_edges = np.histogram(interval, bins=bins)
        
#         # Нормируем до плотности: (i / N) / delta
#         density = counts / (N * step)
        
#         # Середины бинов
#         bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
        
#         # Рисуем полигон плотности
#         plt.plot(
#             bin_centers,
#             density,
#             marker='o',
#             linestyle='-',
#             label=labels[idx],
#             color=colorsLine[idx],
#             markersize=3
#         )

#     plt.legend()
#     plt.grid(alpha=0.6, linestyle='--')
#     plt.tight_layout()
#     plt.show()


# def drawCountEvents(events, labels, colors=['lightcoral', 'olivedrab', 'teal', 'fuchsia', 'red', 'green', 'blue'],t=1):
#     """
#     Строит полигон частот для дискретной случайной величины:
#     K = число событий в случайно выбранном единичном интервале времени.
#     """
#     plt.figure(figsize=(12, 6))

#     for idx, event_series in enumerate(events):
#         if len(event_series) == 0:
#             continue

#         # Шаг 1: Считаем число событий в каждом единичном интервале
#         t_max = int(np.ceil(np.max(event_series)))
#         bins = np.arange(0, t_max + t, t)
#         counts_per_interval, _ = np.histogram(event_series, bins=bins)  # это k₁, k₂, ..., kₙ

#         # Шаг 2: Считаем частоты значений k (0,1,2,...)
#         k_values, frequencies = np.unique(counts_per_interval, return_counts=True)

#         # Шаг 3: Строим полигон частот
#         plt.plot(
#             k_values,
#             frequencies,
#             marker='o',
#             linestyle='-',
#             color=colors[idx % len(colors)],
#             label=labels[idx],
#             markersize=4
#         )

#     plt.legend()
#     plt.grid(True, linestyle='--', alpha=0.6)
#     # plt.xticks(k_values)  # чтобы все целые k были подписаны (можно убрать при большом разбросе)
#     plt.tight_layout()
#     plt.show()

# находит распределение числа событий в выборке за время t
def event_count_distribution(trace, t):
    intervals = np.diff(trace)
    Lambda = 1.0 / np.mean(intervals)

    normTrace = np.multiply(trace, Lambda)

    counts = count_events_in_window(normTrace, t)

    return counts

# считает количество событий в выборке
def count_events_in_window(normTrace, t):
    max_time = normTrace[-1]
    n_windows = int(max_time // t)
    counts = np.zeros(n_windows, dtype=int)

    window_indices = (normTrace // t).astype(int)

    for idx in window_indices:
        if idx < n_windows:
            counts[idx] += 1

    return counts

def empirical_cdf(counts):
    values, freq = np.unique(counts, return_counts=True)
    probs = freq / freq.sum()
    cdf = np.cumsum(probs)
    return values, cdf

def empirical_kolmogorov_distance(v1, f1, v2, f2):
    # Общая сетка для интерполяции
    grid = np.union1d(v1, v2)

    # Интерполяция CDF на общей сетке
    f1_interp = np.interp(grid, v1, f1, left=0.0, right=1.0)
    f2_interp = np.interp(grid, v2, f2, left=0.0, right=1.0)

    abs_diff = np.abs(f1_interp - f2_interp)

    # Расстояние Колмогорова — максимум абсолютной разницы
    D = np.max(abs_diff)

    idx_max = np.argmax(abs_diff)
    x_max = grid[idx_max]
    return D, x_max

# Относительная ошибка
def relativeErr(true, pred):
    return ((true - pred) / pred) * 100
    

    