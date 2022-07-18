product_prices = [1200, 5000, 4500, 7300, 3000, 2100]
covid_cases = [231, 776, 331, 897, 554, 131]
ipl_team_scores = [12, 5, 8, 7, 3, 9]


def get_max(data):
    max = data[0]
    for idx in range(1, len(data)):
        if data[idx] > max:
            max = data[idx]

    print("Max is:", max)
    return max

"""
max = product_prices[0]
for idx in range(1, len(product_prices)):
    if product_prices[idx] > max:
        max = product_prices[idx]

print("Max in product_prices is:", max)

max = covid_cases[0]
for idx in range(1, len(covid_cases)):
    if covid_cases[idx] > max:
        max = covid_cases[idx]

print("Max in covid_cases is:", max)

max = ipl_team_scores[0]
for idx in range(1, len(ipl_team_scores)):
    if ipl_team_scores[idx] > max:
        max = ipl_team_scores[idx]

print("Max in ipl_team_scores is:", max)
"""
result = get_max(product_prices)
print("Max in product_prices is:", result)
print("Max in covid_cases is:", get_max(covid_cases))
print("Max in ipl_team_scores is:", get_max(ipl_team_scores))
