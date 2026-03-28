import core.searchModule as sm
import numpy as np

class Gradient:

    def __init__(self, init_matricies, targets, lr=0.05, steps=1e4, eps=1e-7, patience=250):
        self.init_matricies = init_matricies
        self.targets = targets
        self.size = len(init_matricies[0])
        self.lr = lr
        self.steps = steps
        self.eps = eps
        self.patience = patience

    def matrix_to_vector(self):
        """Преобразует матрицы в векторы параметров"""
        Q, Lambda, D = self.init_matricies

        # Q: все недиагональные элементы
        idx = 0
        Q_vec = np.zeros(self.size ** 2 - self.size)
        for i in range(self.size):
            for j in range(self.size):
                if i != j:
                    Q_vec[idx] = Q[i][j]
                    idx+=1
        
        # Lambda: только диагональ
        Lambda_vec = np.zeros(self.size)
        for i in range(self.size):
            Lambda_vec[i] = Lambda[i][i]
        
        # D: все недиагональные элементы
        idx = 0
        D_vec = np.zeros(self.size ** 2 - self.size)
        for i in range(self.size):
            for j in range(self.size):
                if i != j:
                    D_vec[idx] = D[i][j]
                    idx+=1
        
        return Q_vec, Lambda_vec, D_vec

    def vector_to_matrix(self, Q_vec, Lambda_vec, D_vec):
        """Преобразует векторы параметров обратно в матрицы"""
        # Q: собираем матрицу из недиагональных элементов
        Q = np.zeros((self.size, self.size))
        idx = 0
        for i in range(self.size):
            for j in range(self.size):
                if i != j:
                    Q[i][j] = abs(Q_vec[idx])
                    idx += 1
        # Диагональ = -sum по строке
        row_sums = np.sum(Q, axis=1)
        for i in range(self.size):
            Q[i][i] = -row_sums[i]
        
        # Lambda: диагональная матрица
        Lambda = np.diag(Lambda_vec)
        
        # D: собираем матрицу из недиагональных элементов
        D = np.zeros((self.size, self.size))
        idx = 0
        for i in range(self.size):
            for j in range(self.size):
                if i != j:
                    D[i][j] = np.clip(D_vec[idx], 0, 1)
                    idx += 1
        
        return Q, Lambda, D

    # объединяем все параметры в один вектор с обучаемыми параметрами
    def learn_params(self):
        q_vec, l_vec, d_vec = self.matrix_to_vector()
        params = []
        for i in range(len(q_vec)):
            params.append(q_vec[i])
        for i in range(len(l_vec)):
            params.append(l_vec[i])
        for i in range(len(d_vec)):
            params.append(d_vec[i])

        return np.array(params)

    def unpack_params(self, params):
        q_vec = []
        l_vec = []
        d_vec = []
        idx = 0
        for _ in range(self.size**2 - self.size):
            q_vec.append(params[idx])
            idx+=1

        for _ in range(self.size):
            l_vec.append(params[idx])
            idx+=1

        for _ in range(self.size**2 - self.size):
            d_vec.append(params[idx])
            idx+=1

        q_vec = np.array(q_vec)
        l_vec = np.array(l_vec)
        d_vec = np.array(d_vec)
        return self.vector_to_matrix(q_vec, l_vec, d_vec)

    # функция ошибки
    def loss_fn(self, params):
        Q, Lambda, D = self.unpack_params(params)
        return sm.fit((Q, Lambda, D), *self.targets)

    # функция численного градиента
    def gradient(self, params, eps=0.1):
        """Метод конечных разностей (центральная разность)"""
        grad = np.zeros_like(params)
        for i in range(len(params)):
            params_plus = params.copy()
            params_minus = params.copy()

            # params_plus[i] += eps
            params_minus[i] -= eps

            grad[i] = (self.loss_fn(params_plus) - self.loss_fn(params_minus)) / (2 * eps)

        return grad

    def gradientSPSA(self, params, eps=1e-2):
            """Simultaneous perturbation stochastic approximation (SPSA)"""
            grad = np.zeros_like(params)
            delta = np.random.choice([-1, 1], size=len(params))

            params_plus = params + eps * delta
            params_minus = params - eps * delta

            loss_plus = self.loss_fn(params_plus)
            loss_minus = self.loss_fn(params_minus)

            grad = (loss_plus - loss_minus) / (eps * 2) * delta

            return grad

    def search(self):
        params = self.learn_params()
        best_params = params
        i = 0
        i_pat = 0
        loss = self.loss_fn(best_params)
        best_loss = np.inf
        prevLoss = 0
        while loss > self.eps and i < self.steps:
            # считаем градиент
            grad = self.gradientSPSA(params)
            
            # градиентный спуск
            params = params - self.lr * grad

            # считаем ошибку
            loss = self.loss_fn(params)
            
            if loss < best_loss:
                best_params = params
                best_loss = loss

            # print(i, loss)
            i+=1
            if loss < prevLoss:
                i_pat = 0
            else:
                i_pat+=1
            prevLoss = loss

            if i_pat == self.patience:
                print('early stopping')
                break

            # if i % 1000 == 0:
            #     # self.lr = self.lr / ((i + 1) ** 0.6)
            #     print(i, "loss:", loss)
            #print(i, loss)
        # print("Итераций: ", i)
        return self.unpack_params(best_params), best_loss