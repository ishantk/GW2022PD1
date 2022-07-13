# Set is not stored on Indexes
# It uses Hashing to save data in memory
johns_friends = {"anna", "dave", "kia", "leo", "mark", "dave"}
print(johns_friends, type(johns_friends), hex(id(johns_friends)))

fionnas_friends = {"anna", "harry", "george", "leo", "sim"}
print(fionnas_friends, type(fionnas_friends), hex(id(fionnas_friends)))

mutual_friends = johns_friends.intersection(fionnas_friends)
print(mutual_friends)

johns_friends.add("kim")
print(johns_friends)