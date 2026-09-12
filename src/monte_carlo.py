import numpy as np
import pandas as pd


def monte_carlo_simulation(
    simulations=10_000,
    years=10,
    initial_investment=100_000,

    revenue_mean=35_000,
    revenue_std=3_500,

    cost_mean=20_000,
    cost_std=2_000,

    inflation_mean=0.03,
    inflation_std=0.01,

    interest_mean=0.05,
    interest_std=0.01
):

    results = []

    for simulation in range(simulations):

        inflation = np.random.normal(
            inflation_mean,
            inflation_std
        )

        discount_rate = np.random.normal(
            interest_mean,
            interest_std
        )

        inflation = max(inflation, 0)

        discount_rate = max(
            discount_rate,
            0.001
        )

        npv_value = -initial_investment

        revenue = max(
            np.random.normal(
                revenue_mean,
                revenue_std
            ),
            0
        )

        costs = max(
            np.random.normal(
                cost_mean,
                cost_std
            ),
            0
        )

        for year in range(1, years + 1):

            revenue_t = revenue * (
                1 + inflation
            ) ** year

            costs_t = costs * (
                1 + inflation
            ) ** year

            cash_flow = (
                revenue_t - costs_t
            )

            discounted_cash_flow = (
                cash_flow
                / (1 + discount_rate) ** year
            )

            npv_value += discounted_cash_flow

        results.append({
            "Simulation": simulation + 1,
            "Inflation": inflation,
            "Discount Rate": discount_rate,
            "NPV": npv_value
        })

    return pd.DataFrame(results)