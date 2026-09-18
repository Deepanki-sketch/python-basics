import math

# WEEK 12 — PAIRED t-TEST

def sample_mean(data):
    return sum(data) / len(data)


def sample_variance(data):
    n = len(data)
    mean = sample_mean(data)



def paired_t_test(x, y):
    """
    First calculate:

    D_i = X_i - Y_i

    Then perform one-sample t-test
    on the differences.
    """

    if len(x) != len(y):
        raise ValueError(
            "Both paired samples must have same length."
        )

    differences = [
        xi - yi
        for xi, yi in zip(x, y)
    ]

    n = len(differences)

    d_bar = sample_mean(differences)
    sd = math.sqrt(sample_variance(differences))

    t = d_bar / (sd / math.sqrt(n))

    df = n - 1

    return t, df, differences