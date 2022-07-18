# break and continue
# nested loops
# Functions and Recursion

employees = ["John", "Fionna", "Harry", "Dave", "Kia", "Sim"]
employee_to_found = input("Enter Employee Name: ")
for idx in range(0, len(employees)):

    print("Checking", employee_to_found, "with", employees[idx])

    if employees[idx] == employee_to_found:
        print(employee_to_found, "Found in Data Set")
        break

my_floor = 5
for floor_number in range(1, 11):
    print("Elevator Arrived at Floor #", floor_number)

    if(floor_number == my_floor):
        print("My Floor Arrived:", my_floor)
        break

for idx in range(1, 11):

    if idx <= 5:
        continue

    print("idx is:", idx)

employees_salaries = [45000, 30000, 12000, 90000, 20000, 75000, 55000]
for idx in range(0, len(employees_salaries)):

    if employees_salaries[idx] >= 50000:
        print(employees_salaries[idx])
        continue

    employees_salaries[idx] += 5000
    employees_salaries[idx] += ((idx+1)*500)

print("employees_salaries")
print(employees_salaries)