# johns_cafe_name = 'John\'s Italian Delight'
johns_cafe_name = "John's Italian Delight"
print(johns_cafe_name, type(johns_cafe_name))
print(len(johns_cafe_name))
print(min(johns_cafe_name))
print(max(johns_cafe_name))


johns_cafe_name = """John's Italian Delight
- An Authentic Italian Restaurant
"""

print(johns_cafe_name)

# Raw String -> We need it in Using Regular Expressions :)
# Any Special i.e. escape character will become the part of String
johns_cafe_name = r'John\'s Italian \nDelight'
print(johns_cafe_name)

names = "john, JENNIE, jim, jack, joe"
print(len(names))

# Strings are IMMUTABLE :)
# They are never modified. Modification means a new string in the memory
s1 = names.upper() # lower()
print(names)
print(s1)

s2 = names.capitalize()
print(s2)

s3 = names.replace('j', 'KO')
print(s3)

# s4 = names.title()
s4 = names.swapcase()
print(s4)

# rstrip() | lstrip()
password = input("Enter a Password: ").strip()
print("Password is:", password)

data = "00000000320500"
formatted_data = data.strip('0')
print(formatted_data)

message = "No Internet Connectivity"
print(message.center(60))
print(message.ljust(60))
print(message.rjust(60))


print("545".zfill(50))

quote = "search the candle rather than cursing the darkness"
print(quote.find("sing"))
print(quote.index("the"))
print(quote.rindex("the"))
print(quote[33: ])
