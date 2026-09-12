import pandas as pd

from financial_formulas import (
    real_interest_rate,
    purchasing_power
)


def calculate_real_values(
    nominal_cash_flows,
    inflation_rate
):
    """
    Convert nominal cash flows into real purchasing-power terms.
    """

    real_cash_flows = []

    for year, cash_flow in enumerate(
        nominal_cash_flows
    ):

        real_value = cash_flow / (
            1 + inflation_rate
        ) ** year

        real_cash_flows.append(real_value)

    return real_cash_flows


def inflation_scenario_analysis(
    cash_flows,
    discount_rate,
    inflation_rates
):

    from financial_formulas import npv

    results = []

    for inflation in inflation_rates:

        real_rate = real_interest_rate(
            discount_rate,
            inflation
        )

        real_cash_flows = calculate_real_values(
            cash_flows,
            inflation
        )

        real_npv = npv(
            real_rate,
            real_cash_flows
        )

        results.append({
            "Inflation": inflation,
            "Real Interest Rate": real_rate,
            "Real NPV": real_npv
        })

    return pd.DataFrame(results)