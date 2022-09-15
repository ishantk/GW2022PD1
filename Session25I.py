class Student:

    def __init__(self, roll, name, phone, email, gender):
        self.roll = roll
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender

    def to_csv(self):
        return "{roll},{name},{phone},{email},{gender}\n".format_map(vars(self))


student1 = Student(101, 'John', '+91 99999 11111', 'john@example.com', 'male')
student2 = Student(201, 'Fionna', '+91 99999 22222', 'fionna@example.com', 'female')
data1 = student1.to_csv()
data2 = student2.to_csv()
print(data1)

# file = open("students.csv", "w")
file = open("students.csv", "a")
file.write(data2)
print("Student Saved in File")