import numpy as np
import copy
import math
from core import analysisModule


# Генерация матрицы Q
def GenQ(size, rQ):
    Q = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            Q[i][j] = np.random.uniform(0, rQ)
            Q[i][i] = 0
    diag = np.sum(Q, axis=1)
    for i in range(size):
        Q[i][i] = -diag[i]
    del (diag)
    return Q

# Генерация матрицы Lambda
def GenL(size, rLamb):
    Lambda = np.zeros((size, size))
    for i in range(size):
        Lambda[i][i] = np.random.uniform(0, rLamb)
    return(Lambda)

# Генерация матрциы D
def GenD(size):
    matrix = np.random.rand(size, size)
    np.fill_diagonal(matrix, 0)
    # matrix = np.zeros((size, size))     #для mmpp D = 0
    return matrix

# Генерация случайных параметров
def generateRandomParameters(size, rQ = 10, rLamb = 10):
    Q = GenQ(size, rQ)
    Lambda = GenL(size, rLamb)
    D = GenD(size)
    return Q, Lambda, D

# Функция ошибки
def fit(individual, cvTarget, corrTarget, skewnessTarget = None, kurtosisTarget = None, weights = None):
    Q, Lambda, D = individual
    weight_cv, weight_corr, weight_skew, weight_kurt = 1, 1, 1, 1
    if weights is not None:
        weight_cv = weights[0]
        weight_corr = weights[1]
        weight_skew = weights[2]
        weight_kurt = weights[3]
    meanEmp, varEmp, cvEmp, corrEmp, skewnessEmp, kurtosisEmp = analysisModule.characteristics(Q, Lambda, D)

    if skewnessTarget is None and kurtosisTarget is None:
        error = (
                weight_cv*((cvEmp - cvTarget) / cvTarget) ** 2 +
                weight_corr*((corrEmp - corrTarget) / (1 + abs(corrTarget))) ** 2
        )
        sum_weight = weight_cv + weight_corr
        return error / sum_weight
    elif skewnessTarget is None:
        error = (
                weight_cv*((cvEmp - cvTarget) / cvTarget) ** 2 +
                weight_corr*((corrEmp - corrTarget) / (1 + abs(corrTarget))) ** 2 +
                weight_kurt*((kurtosisEmp - kurtosisTarget) / kurtosisTarget) ** 2
        )
        sum_weight = weight_cv + weight_corr + weight_kurt
        return error / sum_weight
    elif kurtosisTarget is None:
        error = (
                weight_cv*((cvEmp - cvTarget) / cvTarget) ** 2 +
                weight_corr*((corrEmp - corrTarget) / (1 + abs(corrTarget))) ** 2 +
                weight_skew*((skewnessEmp - skewnessTarget) / skewnessTarget) ** 2
        )
        sum_weight = weight_cv + weight_corr + weight_skew
        return error / sum_weight
    elif corrTarget is None:
        error = (
            weight_cv*((cvEmp - cvTarget) / cvTarget) ** 2 +
            weight_skew*((skewnessEmp - skewnessTarget) / skewnessTarget) ** 2 +
            weight_kurt*((kurtosisEmp - kurtosisTarget) / kurtosisTarget) ** 2
        )
        sum_weight = weight_cv + weight_skew + weight_kurt
        return error / sum_weight
    else:
        error = (
                weight_cv*((cvEmp - cvTarget) / cvTarget) ** 2 +
                weight_corr*((corrEmp - corrTarget) / (1 + abs(corrTarget))) ** 2 +
                weight_skew*((skewnessEmp - skewnessTarget) / skewnessTarget) ** 2 +
                weight_kurt*((kurtosisEmp - kurtosisTarget) / kurtosisTarget) ** 2
        )
        sum_weight = weight_cv + weight_corr + weight_skew + weight_kurt
        return error / sum_weight


# Функция для генерации pop_size MAP-потоков со случайными параметрами
def initialize_population(pop_size, size, rQ, rLamb):
    population = []
    for _ in range(pop_size):
        Q, Lambda, D = generateRandomParameters(size, rQ, rLamb)
        population.append([Q,Lambda,D])
    return population

"""_____________________________________________________________________________________"""

# Алгоритм с последовательным перебором параметров
def brute_force_search(sizeMap, cvTarget, corrTarget, pop_size=30, rQ=10, rLamb=10, skewnessTarget = None, kurtosisTarget = None, weights = None):
    """
        pop_size - кол-во генерируемых МАР-потоков для поиска начального решения\n
        sizeMap - размер MAP-потока\n
        cv - искомая вариация\n
        corr = искомая корреляция\n
        rQ - правая граница для Q\n
        rLamb - правая граница для Lambda\n
        skewness - коэффициент асимметрии\n
        kurtosis - коэффициент эксцесса\n
        weights - веса для функции потерь\n
        точность изменяется динамически от последнего найденного решения
    """
    f = open("logSearch.txt", "a")
    best = []
    iter = 0
    Fit = 100
    best_fitness = float('inf')
    pop = None  # Для хранения лучшего индивида

    maxIter = 5000
    #print("Pop")
    while best_fitness > 0.0001 and iter < 1000:
        population = initialize_population(pop_size, sizeMap, rQ, rLamb)
        fitness_values = [fit(individual, cvTarget, corrTarget, skewnessTarget, kurtosisTarget, weights) for individual in population]
        current_best_fitness = min(fitness_values)
        if current_best_fitness < best_fitness:
            best_fitness = current_best_fitness
            pop = population[fitness_values.index(current_best_fitness)]
        iter += 1
        if iter == maxIter:
            over = True
        #print(f"\rИтерация: {iter}, Fit: {Fit}", end="")

    eps = 10 ** (math.floor(math.log10(best_fitness)))
    """if over:
        eps = 10 ** (math.floor(math.log10(abs(best_fitness))) + 1) # Извлекаем точность
        over = False"""

    iter = 0
    best_fitness = float('inf')
    #print("Поиск Q")
    while (eps / 10) < Fit and iter < maxIter:
        Q = GenQ(sizeMap, rQ)
        pop[0] = Q
        Fit = fit(pop, cvTarget, corrTarget, skewnessTarget, kurtosisTarget, weights)
        if Fit < best_fitness:
            best_fitness = Fit
            best = copy.deepcopy(pop)
        iter += 1
        if iter == maxIter:
            over = True
        #print(f"\rИтерация: {iter}, Fit: {Fit}", end="")

    sumIter = iter
    iter = 0
    Fit = 100
    pop = copy.deepcopy(best)
    div = 10

    eps = 10 ** (math.floor(math.log10(best_fitness)))  # Извлекаем точность
    #print("\nПоиск лямбда")

    while (eps / 10) < Fit and iter < maxIter:
        Lambda = GenL(sizeMap, rLamb)
        pop[1] = Lambda
        Fit = fit(pop, cvTarget, corrTarget, skewnessTarget, kurtosisTarget, weights)
        if Fit < best_fitness:
            best_fitness = Fit
            best = copy.deepcopy(pop)
        iter += 1
        if iter == maxIter:
            over = True
        #print(f"\rИтерация: {iter}, Fit: {Fit}", end="")


    eps = 10 ** (math.floor(math.log10(best_fitness)))  # Извлекаем точность

    sumIter += iter
    iter = 0
    Fit = 100
    pop = copy.deepcopy(best)

    #print("\nПоиск D")
    while (eps / 10) < Fit and iter < maxIter:
        D = GenD(sizeMap)
        pop[2] = D
        Fit = fit(pop, cvTarget, corrTarget, skewnessTarget, kurtosisTarget, weights)
        if Fit < best_fitness:
            best_fitness = Fit
            best = copy.deepcopy(pop)
        iter += 1
        #print(f"\rИтерация: {iter}, Fit: {Fit}", end="")

    # mean, var, cvE, corrE, skewnessE, kurtosisE  = analysisModule.characteristics(best[0], best[1], best[2])
    #print(f"\nНайденная вариация: {cvE}")
    #print(f"Найденная корреляция: {corrE}")
    #print(f"Найденный коэф.асимметрии: {skewnessE}")
    #print(f"Найденный коэф.эксцесса: {kurtosisE}")
    #print("Всего итераций: ", sumIter)
    print("Минимальная ошибка:", best_fitness)
    #f.write(f"{cv}, {corr}, {sumIter}\n")
    return best, best_fitness

"""_____________________________________________________________________________________"""
# Алгоритм с перебором параметров MAP-потока в заданной окрестности


def local_search(sizeMap, cvTarget, corrTarget, pop_size=30, rQ=10, rLamb=10, percent = 0.02, skewnessTarget = None, kurtosisTarget = None, enhanced = False, weights = None):
    """
    pop_size - кол-во генерируемых МАР-потоков для поиска начального решения\n
    sizeMap - размерность MAP-потока\n
    cvTarget - искомая вариация\n
    corrTarget - искомая корреляция\n
    rQ - правая граница Q\n
    rLambda - правая граница Lambda\n
    percent - окресность, в которой будут изменяться параметры Q и Lambda\n
    skewnessTarget - коэффициент асимметрии\n
    kurtosisTarget - коэффициент эксцесса\n
    weights - веса для функции потерь
    точность изменяется динамически от последнего найденного решения
    """
    # Ищем начальное решение
    map, Fit = initialGuess(pop_size, sizeMap, cvTarget, corrTarget, rQ, rLamb, skewnessTarget, kurtosisTarget)
    #eps = 10 ** (math.floor(math.log10(abs(Fit))) + 1)  # Извлекаем точность
    if not math.isfinite(Fit) or Fit == 0:
        eps = 1e-6  
    else:
        eps = 10 ** (math.floor(math.log10(Fit)))
    if enhanced:
        # Изменяем параметры в окрестности percent до заданной точности
        map, Fit, newInit = districEnhanced(map, percent, eps / 10, cvTarget, corrTarget, skewnessTarget, kurtosisTarget, weights)
        # если значение ошибки не изменяется, ищется новое начальное решение
        while newInit:
            map, Fit = initialGuess(pop_size, sizeMap, cvTarget, corrTarget, rQ, rLamb, skewnessTarget, kurtosisTarget)
            eps = 10 ** (math.floor(math.log10(Fit)))  # Извлекаем точность
            map, Fit, newInit = districEnhanced(map, percent, eps / 10, cvTarget, corrTarget, skewnessTarget, kurtosisTarget, weights)
    else:
        map = distric(map, percent, eps / 10, cvTarget, corrTarget, skewnessTarget, kurtosisTarget, weights)
    if not math.isfinite(Fit) or Fit == 0:
        eps = 1e-6  
    else:
        eps = 10 ** (math.floor(math.log10(Fit)))

    Q, Lambda, D = map
    best = map
    best_fitness = float('inf')
    iter = 0
    # Отдельный поиск подбор D для заданного eps / 10
    #print("D")
    while (eps / 10) < Fit and iter <= 5000:
        D = GenD(sizeMap)
        Fit = fit([Q, Lambda, D], cvTarget, corrTarget, skewnessTarget, kurtosisTarget, weights)
        if Fit < best_fitness:
            best_fitness = Fit
            best = Q, Lambda, D
        iter += 1
        #print(f"\rИтерация: {iter}, Fit: {Fit}", end="")
    #print("\n", analysisModule.characteristics(best[0], best[1], best[2]))
    print(f"best fit: {best_fitness}")
    return best, best_fitness

# Перебор элементов матриц Q и Lambda в окрестности
"""
    map - матрицы Q, Lambda, D
    percent - окрестность
    eps - точность
    cv - искомая вариация
    corr - искомая корреляция
"""
def distric(map, percent, eps, cv, corr, skewness, kurtosis, weights):      # изменение каждого параметра по отдельности в его окресности
    #print("district")
    bestMap = copy.deepcopy(map)
    size = len(map[0])
    Fit = fit(map, cv, corr, skewness, kurtosis)
    k = 0
    best = float('inf')
    iter = 0

    while eps < Fit and iter < 2:
        Q, Lambda, D = bestMap
        for i in range(size):
            for j in range(size):
                if i != j:
                    Q[i][j] *= (1 + np.random.uniform(-percent, percent))
                else:
                    Q[i][j] = 0
            Q[i][i] = -np.sum(Q[i])
            Lambda[i][i] *= (1 + np.random.uniform(-percent, percent))
        Fit = fit([Q, Lambda, D], cv, corr, skewness, kurtosis, weights)

        if Fit < best:
            best = Fit
            bestMap = Q, Lambda, D
        k += 1
        #print(f"\rИтерация dist: {k}, BestFit: {best}", end="")
        if k == 5000:
            bestMap = copy.deepcopy(map)
            k = 0
            iter += 1
    return bestMap

# Поиск начального решения с перегенерацией всех параметров
def initialGuess(pop_size, sizeMap, cvEmp, corrEmp, rQ, rLamb, skewness, kurtosis):
    best_fitness = float('inf')
    pop = None  # Для хранения лучшего индивида
    iter = 0
    over = False
    #print("\nguess")
    while best_fitness > 0.0001 and iter < 1000:
        population = initialize_population(pop_size, sizeMap, rQ, rLamb)
        fitness_values = [fit(individual, cvEmp, corrEmp, skewness, kurtosis) for individual in population]
        current_best_fitness = min(fitness_values)
        if current_best_fitness < best_fitness:
            best_fitness = current_best_fitness
            pop = population[fitness_values.index(current_best_fitness)]
        iter += 1
        if iter == 3000:
            over = True
    return pop, best_fitness

# Корректировка среднего
def meanMap(map, meanTarget):
    Q, Lambda, D = map
    D0,D1 = analysisModule.getD0D1(Q, Lambda, D)
    R = analysisModule.compute_stationary_distribution(Q)
    k = np.dot(R, np.dot(D1, np.ones(len(R))))
    mean = k ** -1
    koef = meanTarget / mean

    Q = Q / koef
    Lambda = Lambda / koef
    return np.array(Q), np.array(Lambda), np.array(D)

"""________________________________________________________________"""

def districEnhanced(map, percent, eps, cv, corr, skewness, kurtosis, weights):      # изменение каждого параметра по отдельности в его окресности
    #print("district")
    bestMap = copy.deepcopy(map)
    size = len(map[0])
    Fit = fit(map, cv, corr, skewness, kurtosis, weights)
    k = 0
    it = 0
    best = float('inf')
    while eps < Fit:
        Fit_start_of_iter = Fit
        Q, Lambda, D = bestMap
        for i in range(size):
            for j in range(size):
                if i != j:
                    # Сохраняем ошибку до изменений
                    prevFit = fit([Q, Lambda, D], cv, corr, skewness, kurtosis, weights)
                    origQ = Q[i][j]     # сохраняем Qij до изменений
                    Q[i][j] *= (1 + np.random.uniform(0, percent))      # изменяем Qij в большую сторону на percent
                    Q = recoveryQ(Q)    # восстанавливаем Q
                    Fit = fit([Q, Lambda, D], cv, corr, skewness, kurtosis, weights)     # вычисляем ошибку после изменений
                    if prevFit < Fit:       # если ошибка не уменьшилась, пробуем изменить в другую сторону
                        Q[i][j] = origQ     # Qij возвращаем к исходному значению
                        Q[i][j] *= (1 - np.random.uniform(0, percent))   # изменяем Qij в меньшую сторону на percent
                        Q = recoveryQ(Q)    # восстанавливаем Q
                        Fit = fit([Q, Lambda, D], cv, corr, skewness, kurtosis, weights) # вычисляем ошибку после изменений
                        if prevFit < Fit:   # если ошибка опять не уменьшилась, то возвращаемся к исходному Qij
                            Q[i][j] = origQ
                            Q = recoveryQ(Q)
            prevFit = fit([Q, Lambda, D], cv, corr, skewness, kurtosis, weights)     # сохраняем ошибку до изменений Lambda
            origL = Lambda[i][i]    # сохраняем Lambda_i
            Lambda[i][i] *= (1 + percent)   # изменяем Lambda_i в большую сторону на percent
            Fit = fit([Q, Lambda, D], cv, corr, skewness, kurtosis, weights)         # вычисляем ошибку после изменений
            if prevFit < Fit:       # если ошибка не уменьшилась, то возвращаемся к исходной Lambda_i
                Lambda[i][i] = origL        # Lambda_i возвращаем к исходному значению
                Lambda[i][i] *= (1 - percent)   # изменяем Lambda_i в меньшую сторону
                Fit = fit([Q, Lambda, D], cv, corr, skewness, kurtosis, weights)     # вычисляем ошибку после изменений
                if prevFit < Fit:   # если ошибка опять не уменьшилась, то возвращаемся к исходному Lambda_i
                    Lambda[i][i] = origL
                    Fit = prevFit
        #print(f"Fit: {Fit}")
        if abs(Fit - Fit_start_of_iter) < 1e-12: # если предыдущая
            k += 1
        else:
            k = 0

        checkFit = Fit  # сохраняем текущую ошибку
        if Fit < best:
            best = Fit
            bestMap = Q, Lambda, D
            it = 0
        else:
            it += 1

        if it >= 200:
            return bestMap, best, False
        if k >= 200:
            return bestMap, Fit, True
        #print(f"\rИтерация dist: {k}, BestFit: {best}", end="")
        #it += 5000
    return bestMap, Fit, False

# Вспомогательная функция восстанавления Q
def recoveryQ(Q):
    for i in range(len(Q)):
        Q[i][i] = 0
        Q[i][i] = -np.sum(Q[i])
    return Q


def relativeErr(true, pred):
    return ((true - pred) / pred) * 100