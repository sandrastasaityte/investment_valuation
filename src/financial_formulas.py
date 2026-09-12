import numpy as np


def future_value(present_value, interest_rate, periods):
    """
    Calculate the future value of a single cash flow.

    FV = PV * (1 + r)^n
    """
    return present_value * (1 + interest_rate) ** periods


def present_value(future_value_amount, discount_rate, periods):
    """
    Calculate the present value of a future cash flow.

    PV = FV / (1 + r)^n
    """
    return future_value_amount / (1 + discount_rate) ** periods


def future_value_annuity(payment, interest_rate, periods):
    """
    Future value of an ordinary annuity.

    FV = PMT * [((1+r)^n - 1) / r]
    """
    if interest_rate == 0:
        return payment * periods

    return payment * (
        ((1 + interest_rate) ** periods - 1)
        / interest_rate
    )


def present_value_annuity(payment, discount_rate, periods):
    """
    Present value of an ordinary annuity.

    PV = PMT * [1 - (1+r)^(-n)] / r
    """
    if discount_rate == 0:
        return payment * periods

    return payment * (
        (1 - (1 + discount_rate) ** (-periods))
        / discount_rate
    )


def effective_annual_rate(nominal_rate, compounding_periods):
    """
    Convert a nominal interest rate into an effective annual rate.

    EAR = (1 + r/m)^m - 1
    """
    return (
        (1 + nominal_rate / compounding_periods)
        ** compounding_periods
        - 1
    )


def real_interest_rate(nominal_rate, inflation_rate):
    """
    Fisher equation:

    1 + i = (1 + r)(1 + pi)

    r = (1+i)/(1+pi) - 1
    """
    return (
        (1 + nominal_rate)
        / (1 + inflation_rate)
        - 1
    )


def purchasing_power(inflation_rate, periods):
    """
    Approximate purchasing power after inflation.

    Purchasing Power = 1 / (1 + inflation)^n
    """
    return 1 / (1 + inflation_rate) ** periods


def npv(discount_rate, cash_flows):
    """
    Calculate Net Present Value.

    cash_flows[0] should normally be the initial investment.
    """
    return sum(
        cash_flow / (1 + discount_rate) ** period
        for period, cash_flow in enumerate(cash_flows)
    )


def irr(cash_flows):
    """
    Calculate Internal Rate of Return.

    Uses numpy_financial if available.
    """
    import numpy_financial as npf

    return npf.irr(cash_flows)