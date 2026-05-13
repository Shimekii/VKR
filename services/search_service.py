from core.optimization.GradDescent import Gradient
from core.analysis import analysis
from core.search import algorithms

# задача для отдельного потока с поиском параметров
def search_run(args):
    size, mean, cv, corr, skew, kurt, method, extra_params, grad_params = args

    (Q, Lambda, D), loss = METHODS[method](
        sizeMap=size,
        cvTarget=cv,
        corrTarget=corr,
        skewnessTarget=skew,
        kurtosisTarget=kurt,
        **extra_params
    )

    threshold = grad_params[0]  # порог
    use = grad_params[1]        # флаг использования
    # если порог не перепрынут и стоит галочка на использование, то используем градиентный спуск
    if grad_params[1] is not None and threshold < loss and use:
        grad = Gradient([Q, Lambda, D], [cv, corr, skew, kurt], **grad_params[2])
        (Q, Lambda, D), loss = grad.search()

    Q, Lambda, D = algorithms.meanMap([Q, Lambda, D], mean)
    R = analysis.compute_stationary_distribution(Q)
    characteristics = analysis.characteristics(Q, Lambda, D)
    return Q, Lambda, D, R, characteristics, loss

METHODS = {
    "Последовательный перебор": algorithms.brute_force_search,
    "Перебор в окрестности": algorithms.local_search,
}