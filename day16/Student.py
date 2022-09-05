class Student:
    def __init__(self, n="",a=0, s=[], m=[]):
        self.name = n
        self.age = a
        self.subjects = s
        self.marks = m

    def display(self):
        print("NAME       =", self.name)
        print("AGE        =", self.age)
        print("SUBJECTS   =", self.subjects)
        print("MARKS      =", self.marks)


ob = Student()
ob.display()
ob1 = Student("Shilpa", 34, ['Python', 'Math'], [66, 67])
print()
ob1.display()

