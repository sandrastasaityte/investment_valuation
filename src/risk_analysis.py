import numpy as np


def calculate_risk_metrics(npv_values):

    npv_values = np.asarray(npv_values)

    expected_npv = np.mean(npv_values)

    median_npv = np.median(npv_values)

    std_npv = np.std(npv_values)

    probability_of_loss = np.mean(
        npv_values < 0
    )

    p5 = np.percentile(
        npv_values,
        5
    )

    p95 = np.percentile(
        npv_values,
        95
    )

    return {
        "Expected NPV": expected_npv,
        "Median NPV": median_npv,
        "NPV Standard Deviation": std_npv,
        "Probability of NPV < 0": probability_of_loss,
        "P5 NPV": p5,
        "P95 NPV": p95
    }