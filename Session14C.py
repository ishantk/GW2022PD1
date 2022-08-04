# my_data = set()
# my_data = list()
# my_data = dict()

my_data = {} # Dictionary
print(my_data, type(my_data), len(my_data))

my_data = {101: "John", 201: "Fionna", 301: "George", 661: "Harry"}
print(my_data)
print(min(my_data))
print(max(my_data))
print(sum(my_data))

print(my_data[201])
print(my_data.get(201))
my_data.pop(201)
print(my_data)

my_data[775] = "Leo"
print(my_data)

my_data[775] = "Kim"
print(my_data)

# my_data.popitem()
del my_data[775]
print(my_data)


columns = ['active', 'confirmed', 'vaccinated']
covid_cases_ludhiana = {}.fromkeys(columns, 10)
print(covid_cases_ludhiana)

covid_cases_ludhiana['active'] = 120
covid_cases_ludhiana['confirmed'] = 12
covid_cases_ludhiana['vaccinated'] = 12120

print(covid_cases_ludhiana)

items = covid_cases_ludhiana.items()
print(items)

for item in items:
    print(item)

keys = covid_cases_ludhiana.keys()
for key in keys:
    print(key)

for key in covid_cases_ludhiana:
    print(key)
    print(covid_cases_ludhiana[key])