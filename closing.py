"""Calculate closing costs for a home of a variable price"""

import sys

# Fixed costs, expressed in thousands of dollars
_FIXED_COSTS = {
    'appraisal / application fee': 0.5,
    'home inspection': 1,
    'title servicing': 1.5,
    'title insurance': 1,
    'attorney': 0.5,
    'insurance': 1,
}

# Costs that are relative to the principal on the loan,
# expressed as a percentage of the principal
_PRINCIPAL_COSTS = {
    'interest': 0.035 / 12,
    'origination': 0.01,
}

# Costs that are relative to the price of the home,
# expressed as a percentage of the price
_PRICE_COSTS = {
    'tax': 0.01,
    'transfer': 0.005,
}

# Price is the first argument to the program, expressed in thousands
_PRICE = int(sys.argv[1])
# Down payment is typically expressed as a portion of the price,
# but you could set a static amount (if under 20%, need to account for PMI)
_DOWN = _PRICE * 0.2  # TODO: handle PMI
_PRINCIPAL = _PRICE - _DOWN
_COSTS = (
    sum(_FIXED_COSTS.values())
    + _PRINCIPAL * sum(_PRINCIPAL_COSTS.values())
    + _PRICE * sum(_PRICE_COSTS.values())
)
# Print the down payment, closing costs, and the sum of the two
# (rounded to the nearest thousand)
print(round(_DOWN), round(_COSTS), round(_DOWN + _COSTS))
