import math 

def chi_square_gof(observed, expected,
                    estimated_parameters=0):

    if len(observed) != len(expected):
        raise ValueError(
            "Observed and expected must have same length."
        )

    contributions = []

    for O, E in zip(observed, expected):

        if E <= 0:
            raise ValueError(
                "Expected frequency must be positive."
            )

        contribution = (O - E) ** 2 / E

        contributions.append(contribution)

    chi_square = sum(contributions)

    k = len(observed)

    df = k - 1 - estimated_parameters

    return chi_square, df, contributions