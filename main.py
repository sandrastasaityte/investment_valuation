import sys

sys.path.append("src")

from investment_model import (
    create_cash_flow_model,
    evaluate_project
)

from monte_carlo import (
    monte_carlo_simulation
)

from risk_analysis import (
    calculate_risk_metrics
)


def main():

    print("=" * 80)
    print("INVESTMENT PROJECT VALUATION MODEL")
    print("Inflation, Interest Rates and Purchasing Power")
    print("=" * 80)

    # ==================================================
    # 1. BASE CASE ASSUMPTIONS
    # ==================================================

    initial_investment = 100_000
    initial_revenue = 35_000
    revenue_growth = 0.05

    initial_costs = 20_000
    cost_growth = 0.04

    tax_rate = 0.20
    discount_rate = 0.05
    years = 10

    print("\nBASE CASE ASSUMPTIONS")
    print("-" * 80)

    print(f"Initial investment: €{initial_investment:,.2f}")
    print(f"Initial revenue:    €{initial_revenue:,.2f}")
    print(f"Revenue growth:     {revenue_growth:.2%}")
    print(f"Initial costs:      €{initial_costs:,.2f}")
    print(f"Cost growth:        {cost_growth:.2%}")
    print(f"Tax rate:           {tax_rate:.2%}")
    print(f"Discount rate:      {discount_rate:.2%}")
    print(f"Project horizon:    {years} years")

    # ==================================================
    # 2. CASH FLOW MODEL
    # ==================================================

    cash_flow_table, cash_flows = create_cash_flow_model(
        initial_investment=initial_investment,
        initial_revenue=initial_revenue,
        revenue_growth=revenue_growth,
        initial_costs=initial_costs,
        cost_growth=cost_growth,
        tax_rate=tax_rate,
        years=years
    )

    # ==================================================
    # 3. NPV AND IRR
    # ==================================================

    valuation = evaluate_project(
        initial_investment=initial_investment,
        discount_rate=discount_rate,
        cash_flows=cash_flows
    )

    print("\nBASE CASE VALUATION")
    print("-" * 80)

    print(
        f"NPV: €{valuation['NPV']:,.2f}"
    )

    print(
        f"IRR: {valuation['IRR']:.2%}"
    )

    # Investment decision
    if valuation["NPV"] > 0:
        print("Investment decision: ACCEPT")
    else:
        print("Investment decision: REJECT")

    # ==================================================
    # 4. CASH FLOW TABLE
    # ==================================================

    print("\nPROJECT CASH FLOWS")
    print("-" * 80)

    print(
        cash_flow_table.to_string(
            index=False,
            float_format=lambda x: f"{x:,.2f}"
        )
    )

    # ==================================================
    # 5. MONTE CARLO SIMULATION
    # ==================================================

    print("\nMONTE CARLO SIMULATION")
    print("-" * 80)

    print("Number of simulations: 10,000")

    simulations = monte_carlo_simulation(
        simulations=10_000,
        years=years,
        initial_investment=initial_investment
    )

    # ==================================================
    # 6. RISK ANALYSIS
    # ==================================================

    risk = calculate_risk_metrics(
        simulations["NPV"]
    )

    print("\nMONTE CARLO RISK RESULTS")
    print("-" * 80)

    print(
        f"Expected NPV:        €{risk['Expected NPV']:,.2f}"
    )

    print(
        f"Median NPV:          €{risk['Median NPV']:,.2f}"
    )

    print(
        f"NPV Std. Deviation:  €{risk['NPV Standard Deviation']:,.2f}"
    )

    print(
        f"Probability of loss: {risk['Probability of NPV < 0']:.2%}"
    )

    print(
        f"P5 NPV:              €{risk['P5 NPV']:,.2f}"
    )

    print(
        f"P95 NPV:             €{risk['P95 NPV']:,.2f}"
    )

    # ==================================================
    # 7. FINAL INTERPRETATION
    # ==================================================

    print("\nINVESTMENT RISK INTERPRETATION")
    print("-" * 80)

    probability_of_loss = (
        risk["Probability of NPV < 0"]
    )

    if probability_of_loss < 0.10:
        risk_level = "LOW"
    elif probability_of_loss < 0.25:
        risk_level = "MODERATE"
    else:
        risk_level = "HIGH"

    print(
        f"Estimated investment risk level: {risk_level}"
    )

    print(
        f"Probability that NPV is negative: "
        f"{probability_of_loss:.2%}"
    )

    print("\n" + "=" * 80)
    print("MODEL COMPLETED")
    print("=" * 80)


if __name__ == "__main__":
    main()