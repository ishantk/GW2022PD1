names = "john, jennie, jim, jack, joe"
print(len(names))
print(names[1])             # o
print(names[len(names)-1])  # e

partitioned_names = names.split(", ")
print(partitioned_names, type(partitioned_names))

s1 = names.replace("john", "mike")
print(s1)
print(names)

contacts = [
    "JOHN",
    "fionna",
    "anna",
    "Dave",
    "Frank",
    "kim",
    "kia",
    "joel",
]

search_keyword = input("Enter Keyword: ")
print("search_keyword:", search_keyword)

for contact in contacts:
    # if contact.lower().startswith(search_keyword.lower()):
    if contact.lower().__contains__(search_keyword.lower()):
        print(contact)

name = "John"
age = 30
email = "john@example.com"

contact = {
    'name':"John",
    'age': 30,
    'email': "john@example.com"
}

print(name, age, email)
print("name is", name, "age is", age, "email is", email)

print("name is {} and age is {} and email is {}".format(name, age, email))
print("name is {1} and age is {0} and email is {2}".format(name, age, email))
print("name is {nm} and age is {age} and email is {email}".format(nm=name, age=age, email=email))
print("name is {name} and age is {age} and email is {email}".format_map(contact))

bill = 125.34567
print("bill amount:", bill)
print("bill amount: {0: .2f}".format(bill))