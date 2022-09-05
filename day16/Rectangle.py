class Rectangle:
    def __init__(self):
        self.width = 0
        self.breadth = 0

    def set_data(self):
        self.width = int(input("Please enter width:"))
        self.breadth = int(input("Please enter breadth:"))

    def calculate(self):
        self.area = self.width * self.breadth
        self.perimeter = 2 * (self.width + self.breadth)

    def display(self):
        print("WIDTH                      = ", self.width)
        print("BREADTH                    = ", self.breadth)
        print("AREA                       = ", self.area)
        print("PERIMETER                  = ", self.perimeter)


ob = Rectangle()
ob.set_data()
ob.calculate()
print()
ob.display()

ob1 = Rectangle()
Rectangle.set_data(ob1)
Rectangle.calculate(ob1)
print()
Rectangle.display(ob1)