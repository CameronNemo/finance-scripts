rate = 0.07
target = 750
current = 29 + 69 + 89
labor = current
contrib = 20 + 6 + 8 + 25
years = 0
while current < target:
    years += 1
    current *= 1 + rate
    current += contrib
    labor += contrib
print(years, round(current))
print(round(current - labor), round(labor))
