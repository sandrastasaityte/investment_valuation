import pandas as pd

from financial_formulas import npv, irr


def create_cash_flow_model(
    initial_investment=100_000,
    initial_revenue=35_000,
    revenue_growth=0.05,
    initial_costs=20_000,
    cost_growth=0.04,
    tax_rate=0.20,
    years=10
):
    """
    Create an investment project's annual operating cash flows.
    """

    rows = []

    for year in range(1, years + 1):

        revenue = initial_revenue * (
            1 + revenue_growth
        ) ** (year - 1)

        costs = initial_costs * (
            1 + cost_growth
        ) ** (year - 1)

        operating_profit = revenue - costs

        taxes = max(operating_profit, 0) * tax_rate

        net_cash_flow = operating_profit - taxes

        rows.append({
            "Year": year,
            "Revenue": revenue,
            "Costs": costs,
            "Operating Profit": operating_profit,
            "Taxes": taxes,
            "Net Cash Flow": net_cash_flow
        })

    df = pd.DataFrame(rows)

    cash_flows = [-initial_investment] + (
        df["Net Cash Flow"].tolist()
    )

    return df, cash_flows


def evaluate_project(
    initial_investment,
    discount_rate,
    cash_flows
):
    """
    Calculate project NPV and IRR.
    """

    project_npv = npv(
        discount_rate,
        cash_flows
    )

    project_irr = irr(cash_flows)

    return {
        "NPV": project_npv,
        "IRR": project_irr
    }