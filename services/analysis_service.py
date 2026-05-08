from core.analysis import analysis
from core.map.MAP import MAP


def compareMapWithTrace(mapProcess, events):
    tmp_map = MAP(*mapProcess)
    n_max = max(events) + 5
    probs = tmp_map.event_count_distribution(n_max, t=5)
    cdf_theory = analysis.np.cumsum(probs)
    values_theory = analysis.np.arange(len(cdf_theory))
    values_emp, cdf_emp = analysis.empirical_cdf(events)
    ks, ksx = analysis.empirical_kolmogorov_distance(values_emp, cdf_emp, values_theory, cdf_theory)
    return (values_emp, cdf_emp, values_theory, cdf_theory, ks, ksx)

def compareTraces(trace1, trace2, t):
    counts1 = analysis.event_count_distribution(trace1, t)
    counts2 = analysis.event_count_distribution(trace2, t)
    v1, cdf1 = analysis.empirical_cdf(counts1)
    v2, cdf2 = analysis.empirical_cdf(counts2)
    ks, ksx = analysis.empirical_kolmogorov_distance(v1, cdf1, v2, cdf2)
    return (v1, cdf1, ks, ksx, v2, cdf2)

def getInfoForTrace(trace):
    return analysis.analysis(trace)
    
def getCdfForTrace(trace):
    counts = analysis.event_count_distribution(trace, 5)
    v, cdf = analysis.empirical_cdf(counts)
    return counts, v, cdf

def getRelativeErr(true, emp):
    return analysis.relativeErr(true, emp)
