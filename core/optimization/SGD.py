import torch
from core.analysis import analysis as am
import numpy as np

#device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
device = 'cpu'

"""Stohastic gradient descent"""

def torch_fit(individual, cvTarget, corrTarget, weights, skewnessTarget = None, kurtosisTarget = None):
    Q, Lambda, D = individual
    meanEmp, varEmp, cvEmp, corrEmp, skewnessEmp, kurtosisEmp = torch_characteristics(Q, Lambda, D)

    weight_cv = weights[0]
    weight_corr = weights[1]
    weight_skew = weights[2]
    weight_kurt = weights[3]

    cvTarget_tensor = torch.tensor(cvTarget, dtype=Q.dtype, device=device)
    corrTarget_tensor = torch.tensor(corrTarget, dtype=Q.dtype, device=device)

    if skewnessTarget is None and kurtosisTarget is None:
        error = (
                weight_cv*((cvEmp - cvTarget_tensor) / cvTarget_tensor) ** 2 +
                weight_corr*((corrEmp - corrTarget_tensor) / (1 + torch.abs(corrTarget_tensor))) ** 2
        )
        sum_weights = weight_cv + weight_corr
        return error / sum_weights
    elif skewnessTarget is None:
        kurtosisTarget_tensor = torch.tensor(kurtosisTarget, dtype=Q.dtype, device=device)
        error = (
                weight_cv*((cvEmp - cvTarget_tensor) / cvTarget_tensor) ** 2 +
                weight_corr*((corrEmp - corrTarget_tensor) / (1 + torch.abs(corrTarget_tensor))) ** 2 +
                weight_kurt*((kurtosisEmp - kurtosisTarget_tensor) / kurtosisTarget_tensor) ** 2
        )
        sum_weights = weight_cv + weight_corr + weight_kurt
        return error / sum_weights
    elif kurtosisTarget is None:
        skewnessTarget_tensor = torch.tensor(skewnessTarget, dtype=Q.dtype, device=device)
        error = (
                weight_cv*((cvEmp - cvTarget_tensor) / cvTarget_tensor) ** 2 +
                weight_corr*((corrEmp - corrTarget_tensor) / (1 + torch.abs(corrTarget_tensor))) ** 2 +
                weight_skew*((skewnessEmp - skewnessTarget_tensor) / skewnessTarget_tensor) ** 2
        )
        sum_weights = weight_cv + weight_corr + weight_skew
        return error / sum_weights
    else:
        skewnessTarget_tensor = torch.tensor(skewnessTarget, dtype=Q.dtype, device=device)
        kurtosisTarget_tensor = torch.tensor(kurtosisTarget, dtype=Q.dtype, device=device)
        error = (
                weight_cv*((cvEmp - cvTarget_tensor) / cvTarget_tensor) ** 2 +
                weight_corr*((corrEmp - corrTarget_tensor) / (1 + torch.abs(corrTarget_tensor))) ** 2 +
                weight_skew*((skewnessEmp - skewnessTarget_tensor) / skewnessTarget_tensor) ** 2 +
                weight_kurt*((kurtosisEmp - kurtosisTarget_tensor) / kurtosisTarget_tensor) ** 2
        )
        sum_weights = weight_cv + weight_corr + weight_skew + weight_kurt
        return error / sum_weights

def torch_compute_stationary_distribution(Q):
    n = Q.shape[0]

    # Добавляем нормировочное уравнение
    A = torch.vstack((Q.T, torch.ones(n, device=device)))  # Транспонируем Q и добавляем строку
    b = torch.zeros(n + 1, device=device)  # Вектор свободных членов
    b[-1] = 1  # Нормировочное уравнение

    solution = torch.linalg.lstsq(A, b.unsqueeze(1)).solution.squeeze()
    R = torch.clamp(solution, min=0)
    R = R / torch.sum(R)
    return R

def torch_getD0D1(Q, Lambda, D):
    B = Q * D
    D1 = Lambda + B
    D0 = Q - D1
    return D0, D1


def torch_characteristics(Q, Lambda, D=None):
    """Полная PyTorch версия characteristics"""
    if D is None:
        D0, D1 = torch_getD0D1(Q, Lambda)
    else:
        D0, D1 = torch_getD0D1(Q, Lambda, D)
    
    R = torch_compute_stationary_distribution(Q)

    k = torch.dot(R, torch.matmul(D1, torch.ones(len(R), device=device)))
    mean = k ** -1

    BQ = torch.linalg.inv(-D0 + torch.eye(D0.shape[0], device=device) * 1e-8)
    E = torch.ones(len(R), device=device)

    # Дисперсия
    temp1 = 2 * k * R
    temp2 = torch.matmul(temp1, BQ)
    temp3 = torch.dot(temp2, E) - 1
    var = temp3 / (k ** 2)

    # Корреляция
    cTemp1 = (k ** -1) * R
    cTemp2 = torch.matmul(cTemp1, BQ)
    cTemp3 = torch.matmul(cTemp2, D1)
    cTemp4 = torch.matmul(cTemp3, BQ)
    cTemp5 = torch.dot(cTemp4, E) - (k ** -2)
    corr = cTemp5 / (var)
    
    CV = torch.sqrt(var) / mean

    # Моменты - ИСПРАВЛЕННЫЕ ВЫЧИСЛЕНИЯ
    # Вычисляем BQ^2, BQ^3 заранее
    BQ2 = torch.matmul(BQ, BQ)
    BQ3 = torch.matmul(BQ2, BQ)
    
    M1 = mean
    M2 = var + mean**2
    M3 = 6 * torch.matmul(torch.matmul(R, BQ2), E) / k  # R @ BQ2 @ E
    M4 = 24 * torch.matmul(torch.matmul(R, BQ3), E) / k  # R @ BQ3 @ E

    mu2 = M2 - M1**2
    mu3 = M3 - 3 * M1 * M2 + 2 * M1**3
    mu4 = M4 - 4 * M1 * M3 + 6 * M1**2 * M2 - 3 * M1**4

    skewness = mu3 / (var**1.5)
    kurtosis = mu4 / (var**2) - 3

    return mean, var, CV, corr, skewness, kurtosis

def recoveryMatrixToTensor(Q, Lambda, D):
    with torch.no_grad():
        # Для Q: все недиагональные элементы положительные, диагональ = отрицательная сумма строки
        Q_new = torch.clone(Q)
        
        # Обнуляем диагональ и делаем недиагональные элементы положительными
        Q_new = Q_new - torch.diag(torch.diag(Q_new))  # обнуляем диагональ
        Q_new = F.softplus(Q_new)  # все недиагональные элементы > 0
        
        # Вычисляем диагональ как отрицательную сумму по строке
        row_sums = torch.sum(Q_new, dim=1)
        Q_new = Q_new - torch.diag(row_sums)  # устанавливаем диагональ
        
        # Для Lambda: только положительная диагональ, остальные 0
        Lambda_new = torch.zeros_like(Lambda)
        diag_lambda = F.softplus(torch.diag(Lambda))  # положительная диагональ
        Lambda_new = Lambda_new + torch.diag(diag_lambda)
        
        # Для D: значения [0,1], диагональ = 0
        D_new = torch.sigmoid(D)  # все элементы [0,1]
        D_new = D_new - torch.diag(torch.diag(D_new))  # обнуляем диагональ
    
    # Сохраняем градиенты
    Q_constrained = Q + (Q_new - Q).detach()
    Lambda_constrained = Lambda + (Lambda_new - Lambda).detach()
    D_constrained = D + (D_new - D).detach()
    
    #print("Q:\n", Q_constrained)
    #print("Lambda\n", Lambda_constrained)
    #print("D:\n", D_constrained)
    return Q_constrained, Lambda_constrained, D_constrained


def create_learnable_matrices(size, initial_Q, initial_Lambda, initial_D):
    """Создает векторы обучаемых параметров"""
    
    # Преобразуем начальные матрицы в векторы
    Q_vec, Lambda_vec, D_vec = matrix_to_vector(
        torch.tensor(initial_Q, dtype=torch.float32, device=device),
        torch.tensor(initial_Lambda, dtype=torch.float32, device=device), 
        torch.tensor(initial_D, dtype=torch.float32, device=device),
        size
    )
    
    # Создаем обучаемые параметры
    Q_params = torch.nn.Parameter(Q_vec)
    Lambda_params = torch.nn.Parameter(Lambda_vec)
    D_params = torch.nn.Parameter(D_vec)
    
    return Q_params, Lambda_params, D_params

def build_matrices_from_params(Q_params, Lambda_params, D_params, size):
    """Собирает матрицы из векторных параметров"""
    return vector_to_matrix(Q_params, Lambda_params, D_params, size)

def matrix_to_vector(Q, Lambda, D, size):
    """Преобразует матрицы в векторы параметров"""
    # Q: все недиагональные элементы
    Q_vec = []
    for i in range(size):
        for j in range(size):
            if i != j:
                Q_vec.append(Q[i, j])
    Q_vec = torch.tensor(Q_vec, dtype=torch.float32, device=device)
    
    # Lambda: только диагональ
    Lambda_vec = torch.diag(Lambda)
    
    # D: все недиагональные элементы
    D_vec = []
    for i in range(size):
        for j in range(size):
            if i != j:
                D_vec.append(D[i, j])
    D_vec = torch.tensor(D_vec, dtype=torch.float32, device=device)
    
    return Q_vec, Lambda_vec, D_vec

def vector_to_matrix(Q_vec, Lambda_vec, D_vec, size):
    """Преобразует векторы параметров обратно в матрицы"""
    # Q: собираем матрицу из недиагональных элементов
    Q = torch.zeros(size, size, dtype=torch.float32, device=device)
    idx = 0
    for i in range(size):
        for j in range(size):
            if i != j:
                Q[i, j] = torch.abs(Q_vec[idx])
                idx += 1
    # Диагональ = -sum по строке
    row_sums = torch.sum(Q, dim=1)
    for i in range(size):
        Q[i, i] = -row_sums[i]
    
    # Lambda: диагональная матрица
    Lambda = torch.diag(Lambda_vec)
    
    # D: собираем матрицу из недиагональных элементов
    D = torch.zeros(size, size, dtype=torch.float32, device=device)
    idx = 0
    for i in range(size):
        for j in range(size):
            if i != j:
                D[i, j] = torch.sigmoid(D_vec[idx])
                idx += 1
    
    return Q, Lambda, D

def sgd_optimization(sizeMap, cvTarget, corrTarget, skewnessTarget=None, kurtosisTarget=None, num_epochs=1000, lr=0.05, eps=1e-7, patience=500, weights = [1,1,1,1]):
    Q_np, Lambda_np, D_np = am.generateRandomParameters(sizeMap, 'map', rQ=10, rLamb=10)
    # Создаем параметры
    Q_params, Lambda_params, D_params = create_learnable_matrices(sizeMap, Q_np, Lambda_np, D_np)
    
    optimizer = torch.optim.Adam([Q_params, Lambda_params, D_params], lr=lr)
    losses = []
    loss = 1
    epoch = 1

    # инициализация для хранения лучших результатов
    best_loss = float('inf')
    best_state_dict = None
    epochs_no_improve = 0

    while loss > eps:
        optimizer.zero_grad()
        
        # Собираем матрицы из параметров (ограничения выполняются автоматически)
        Q, Lambda, D = build_matrices_from_params(Q_params, Lambda_params, D_params, sizeMap)
        
        individual = (Q, Lambda, D)
        loss = torch_fit(individual, cvTarget, corrTarget, weights, skewnessTarget, kurtosisTarget)

        loss.backward()
        optimizer.step()
        
        current_loss = loss.item()
        losses.append(current_loss)

        # Early stopping
        if current_loss < best_loss:
            best_loss = current_loss
            # Сохраняем *копию* состояния параметров
            best_state_dict = {
                'Q': Q_params.clone().detach(),
                'Lambda': Lambda_params.clone().detach(),
                'D': D_params.clone().detach()
            }
            epochs_no_improve = 0
        else:
            epochs_no_improve += 1

        if epochs_no_improve >= patience:
            print(f"Loss не уменьшается")
            break

        if epoch % 500 == 0:
            with torch.no_grad():
                mean, var, cv, corr, skew, kurt = torch_characteristics(Q, Lambda, D)
                print(f"Epoch: {epoch}")
                print(f"    Loss: {current_loss}")
                print(f"    CV: {cv.item():.4f} (target: {cvTarget})")
                print(f"    corr: {corr.item():.4f} (target: {corrTarget})")
                if skewnessTarget is not None:
                    print(f"    skew: {skew.item():.4f} (target: {skewnessTarget})")
                if kurtosisTarget is not None:
                    print(f"    kurt: {kurt.item():.4f} (target: {kurtosisTarget})")
                print()
        epoch += 1
    
    # Возвращаем финальные матрицы
    with torch.no_grad():
        Q_tensor, Lambda_tensor, D_tensor = build_matrices_from_params(Q_params, Lambda_params, D_params, sizeMap)
        Q_final, Lambda_final, D_final = fromTensor(Q_tensor, Lambda_tensor, D_tensor)
    
    return (Q_final, Lambda_final, D_final), current_loss

def fromTensor(Q, Lambda, D):
    Q_orig = Q.detach().numpy()
    Lambda_torch = Lambda.detach().numpy()
    D_orig = D.detach().numpy()
    #Q_orig = SGD.sm.recoveryQ(Q_orig)
    Lambda_orig = np.zeros((len(Lambda_torch), len(Lambda_torch)))
    for i in range(len(Lambda_torch)):
        Lambda_orig[i][i] = Lambda_torch[i][i]
    return Q_orig, Lambda_orig, D_orig