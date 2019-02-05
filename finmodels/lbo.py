class LBOModel:
    def __init__(self, acquisition_price, equity_percentage, debt_interest_rate, years):
        """
        Initializes the LBOModel instance.

        Parameters:
        - acquisition_price (float): The purchase price of the target company.
        - equity_percentage (float): The percentage of acquisition price funded by equity.
        - debt_interest_rate (float): Annual interest rate on debt.
        - years (int): Number of years for the projection period.
        """
        self.acquisition_price = acquisition_price
        self.equity_percentage = equity_percentage
        self.debt_interest_rate = debt_interest_rate
        self.years = years
        self.equity_investment = acquisition_price * equity_percentage
        self.debt_financing = acquisition_price - self.equity_investment

    def calculate_free_cash_flows(self):
        """
        Calculates projected free cash flows for each year.

        Returns:
        - list: Projected free cash flows for each year.
        """
        # Simplified example: Assuming constant free cash flows for demonstration
        average_free_cash_flow = 50
        free_cash_flows = [average_free_cash_flow] * self.years
        return free_cash_flows

    def calculate_debt_payments(self):
        """
        Calculates annual debt payments based on debt financing and interest rate.

        Returns:
        - list: Annual debt payments for each year.
        """
        debt_payments = [self.debt_financing * self.debt_interest_rate] * self.years
        return debt_payments

    def calculate_equity_returns(self):
        """
        Calculates equity returns for each year.

        Returns:
        - list: Equity returns for each year.
        """
        free_cash_flows = self.calculate_free_cash_flows()
        debt_payments = self.calculate_debt_payments()

        equity_returns = [free_cash_flow - debt_payment for free_cash_flow, debt_payment
                          in zip(free_cash_flows, debt_payments)]

        return equity_returns



