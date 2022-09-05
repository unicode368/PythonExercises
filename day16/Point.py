class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def set_data(self, a, b):
        self.x = a
        self.y = b

    def __str__(self):
        return "x = " + str(self.x) + " y = " + str(self.y)

    def compare(self, other):
        return self.x == other.x and self.y == other.y


obj1 = Point()
obj2 = Point()
obj1.set_data(2, 3)
obj2.set_data(22, 3)
print(obj1)
print(obj2)
if obj1.compare(obj2):
    print("Obj 1 and 2 are equal")
else:
    print("not equal")