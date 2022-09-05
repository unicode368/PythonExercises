class Employee:
    def __init__(self):
        self.id = 0
        self.name = ""

    def set_data(self):
        self.id = int(input("Enter the id = "))
        self.name = input("Enter the name = ")

    def get_data(self):
        return self.id, self.name

    def __str__(self):
        s = "ID = " + str(self.id) + "\nNAME = " + self.name
        return s


ob = Employee()
print(ob)
ob.set_data()
print()
print(ob.get_data())
print()
print(ob)

