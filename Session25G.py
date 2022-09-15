ref = lambda x=2, y=2 : x**y
print(ref())
print(ref(2,3))

compute_taxes = lambda amount = float(input("Enter Amount: ")), taxes = 0.18 : amount + (amount*taxes)
print(compute_taxes())

ref1 = lambda x, y: x + y
ref2 = lambda a, b: a * b
#                       4      **   4
ref3 = lambda p, q: ref1(p, q) ** ref2(p, q)
print(ref3(p=2, q=2))