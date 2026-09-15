import math

def beta_binomial_posterior(alpha, beta, successes, n):
    """
    Prior: Beta(alpha, beta)
    Data: successes in n trials

    Posterior:
    Beta(alpha + successes,
         beta + n - successes)
    """
    return (
        alpha + successes,
        beta + n - successes
    )


def beta_mean(alpha, beta):
    return alpha / (alpha + beta)


def beta_mode(alpha, beta):
    """
    Valid when alpha > 1 and beta > 1
    """
    if alpha <= 1 or beta <= 1:
        return None

    return (alpha - 1) / (alpha + beta - 2)


def gamma_poisson_posterior(alpha, beta, data):
    """
    Gamma(alpha, beta) prior
    Poisson observations

    Posterior:
    Gamma(alpha + sum(data),
          beta + n)
    """
    n = len(data)
    total = sum(data)

    return (
        alpha + total,
        beta + n
    )


def gamma_mean(alpha, beta):
    # Rate parameterization used in notes
    return alpha / beta


def exponential_gamma_posterior(a, b, data):
    """
    Gamma(a,b) prior
    Exponential observations

    Posterior:
    Gamma(a+n, b+sum(data))
    """
    n = len(data)
    total = sum(data)

    return (
        a + n,
        b + total
    )
