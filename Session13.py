class Patient:

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.next = None
        self.previous = None

    def show(self):
        print(self.name, self.gender, self.age)

class PatientsQueue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        print("PatientsQueue Created...")

    def enqueue(self, patient):
        self.size += 1

        if self.head is None:
            self.head = patient
            self.tail = patient
        else:
            self.tail.next = patient
            patient.previous = self.tail
            self.tail = patient

    def dequeue(self):
        if self.size != 0:
            self.size -= 1
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            print("No Patient Yet :)")

    def iterate(self):
        print("ITERATING QUEUE")
        temp = self.head
        while True:
            temp.show()
            temp = temp.next

            if temp.next is None:
                temp.show()
                break

    def peek(self, option=1):
        if option == 1:
            return self.head
        else:
            return self.tail


queue = PatientsQueue()
print("Size of Queue is:", queue.size)
queue.enqueue(Patient(name="John", gender="Male", age=40))
queue.enqueue(Patient(name="Fionna", gender="Female", age=42))
queue.enqueue(Patient(name="Jennie", gender="Female", age=32))
queue.enqueue(Patient(name="Kim", gender="Male", age=77))
queue.enqueue(Patient(name="George", gender="Male", age=65))

queue.dequeue()
print("Size of Queue Now is:", queue.size)
queue.peek().show()

queue.iterate()

