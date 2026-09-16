import math 

#  LIKELIHOOD RATIO

def likelihood_ratio(L_H0, L_MLE):
    """
    Lambda = L(H0) / L(MLE)

    -2 ln(Lambda)
    """

    Lambda = L_H0 / L_MLE

    statistic = -2 * math.log(Lambda)

    return Lambda, statistic


