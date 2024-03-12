class IPOModel:
    def __init__(self, initial_valuation, funds_raised, operating_income, growth_rate, years):
        self.initial_valuation = initial_valuation
        self.funds_raised = funds_raised
        self.operating_income = operating_income
        self.growth_rate = growth_rate
        self.years = years

    def calculate_ipo_valuation(self):
        # Calculate the IPO valuation using a simple discounted cash flow (DCF) model
        discount_factor = 1 / (1 + self.growth_rate)
        future_cash_flows = [self.operating_income * (discount_factor ** year) for year in range(1, self.years + 1)]
        total_cash_flows = sum(future_cash_flows)
        ipo_valuation = self.initial_valuation + total_cash_flows + self.funds_raised
        return ipo_valuation

    def print_summary(self):
        ipo_valuation = self.calculate_ipo_valuation()
        print(f"IPO Valuation after {self.years} years: ${ipo_valuation:,.2f}")


# Example usage
#initial_valuation = 500000000  # Initial company valuation before IPO
#funds_raised = 100000000  # Funds raised during the IPO
#operating_income = 75000000  # Annual operating income before IPO
#growth_rate = 0.05  # Annual growth rate of operating income
#years = 5  # Number of years for the IPO model

#ipo_model = IPOModel(initial_valuation, funds_raised, operating_income, growth_rate, years)
#ipo_model.print_summary()
