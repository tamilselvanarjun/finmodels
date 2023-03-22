class IPOModel:
    def __init__(self, initial_valuation, funds_raised, operating_income, growth_rate, years):
        self.initial_valuation = initial_valuation
        self.funds_raised = funds_raised
        self.operating_income = operating_income
        self.growth_rate = growth_rate
        self.years = years

    def calculate_ipo_valuation(self):
        # Calculate the IPO valuation using a simple discounted cash flow (DCF) model.
        discount_factor = 1 + self.growth_rate
        future_cash_flows = [self.operating_income * (discount_factor ** year) for year in range(1, self.years + 1)]
        total_cash_flows = sum(future_cash_flows)
        ipo_valuation = self.initial_valuation + total_cash_flows + self.funds_raised
        return ipo_valuation

    def print_summary(self):
        ipo_valuation = self.calculate_ipo_valuation()
        print(f"IPO Valuation after {self.years} years: ${ipo_valuation:,.2f}")

