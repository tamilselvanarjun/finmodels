def calculate_dcf(cash_flows, discount_rate):
    """
    Calculate the Discounted Cash Flow (DCF) valuation.

    Parameters:
    - cash_flows (list or array): List or array of future cash flows representing the cash inflows or outflows.
    - discount_rate (float): The discount rate used to calculate the present value of future cash flows.

    Returns:
    - float: The present value of the cash flows based on the DCF valuation method.
    """
    dcf_value = sum(cf / (1 + discount_rate) ** i for i, cf in enumerate(cash_flows))
    return dcf_value
