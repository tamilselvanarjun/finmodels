# financial_models/dcf.py
def calculate_dcf(cash_flows, discount_rate):
    """
    Calculate the Discounted Cash Flow (DCF) valuation.

    Parameters:
    - cash_flows: List or array of future cash flows
    - discount_rate: Discount rate used in the calculation

    Returns:
    - DCF value
    """
    dcf_value = sum(cf / (1 + discount_rate) ** (i + 1) for i, cf in enumerate(cash_flows))
    return dcf_value
