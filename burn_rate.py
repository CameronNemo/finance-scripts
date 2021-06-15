"""determine the longevity of a nest egg after a certain number years of funding"""

def compound_interest_w_inflow(principal, rate, years, inflow, inflow_rate):
    if years == 0:
        return principal
    new_principal = ((principal * (1 + rate)) + inflow)
    if years == 1:
        return new_principal
    return compound_interest_w_inflow(
        new_principal, rate, years - 1, inflow * (1 + inflow_rate), inflow_rate
    )

def burn(funding, expenses, wd_rate=0.02):
    wd_gross = funding * wd_rate
    wd_net = wd_gross - expenses
    wd_years = None
    if wd_net < 0:
        wd_years = round(-1 * funding / wd_net, 1)
    return wd_gross, wd_net, wd_years


fund = 54678
net_pay = 43163 - 6000  # assuming Roth IRA contributions
expenses_now = {
    'housing': 100 * 12,
    'utilities': 85 * 12,
    'telecommunications': 15 * 12,
    'food': 200 * 12,
    'car_insurance': 1000,
    'car_maintenance': 500,
}
expenses_future = {
    'housing': 1300 * 12,
    'utilities': 40 * 12,
    'telecommunications': 50 * 12,
}


free_cash_flow_now = net_pay - (sum(expenses_now.values()))
funding_two = compound_interest_w_inflow(fund, 0.06, 2, free_cash_flow_now, 0.03)
gross, net, years = burn(funding_two, (sum(expenses_now.values()) + sum(expenses_future.values())))

free_cash_flow_future = (net_pay * 1.03 * 1.03 * 1.01) - (sum(expenses_now.values()) + sum(expenses_future.values()))
funding_five = compound_interest_w_inflow(funding_two, 0.06, 3, free_cash_flow_future, 0.03)
gross, net, years = burn(funding_five, (sum(expenses_now.values()) + sum(expenses_future.values())))

if __name__ == '__main__':
    print(2, round(funding_two), round(gross), round(net), years)
    print(5, round(funding_five), round(gross), round(net), years)
