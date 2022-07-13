johns_age = 20
# Copy Operation
fionna_age = johns_age
print("johns_age HashCode:", hex(id(johns_age)))
print("fionna_age HashCode:", hex(id(fionna_age)))

# Update Operation
#fionna_age = 30
#print("fionna_age HashCode After Update:", hex(id(fionna_age)))

del johns_age
del fionna_age
# print("johns_age:", johns_age)      # 20
print("fionna_age:", fionna_age)