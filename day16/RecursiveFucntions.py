class RecursiveFunctions:
    def __init__(self, input):
        self.input = input

    def refresh(self, init_val):
        self.input = init_val

    def leftshiftList(self, shift_num):
        if shift_num == 0:
            return
        else:
            i = 1
            res = []
            for j in range(len(self.input)):
                res.append(self.input[i % len(self.input)])
                i += 1
            self.input = res
            self.leftshiftList(shift_num - 1)

    def rightshiftList(self, shift_num):
        if shift_num == 0:
            return
        else:
            i = -1
            res = []
            for j in range(len(self.input)):
                res.append(self.input[i])
                i += 1
            self.input = res
            self.rightshiftList(shift_num - 1)

    def toggleCase(self, start=0):
        if len(self.input) - 1 == start:
            return
        else:
            self.input[start] = self.input[start].swapcase()
            self.toggleCase(start + 1)

    def perfectNumber(self, res, divisor):
        if res > self.input:
            print("Number is non-perfetc!1!")
            return
        if divisor > self.input // 2:
            if res == self.input:
                print("Number is perfetc")
            else:
                print("Number is non-perfetc!1!")
        else:
            if self.input % divisor == 0:
                res += divisor
            self.perfectNumber(res, divisor + 1)

    def primeNum(self, divisor):
        if self.input == 1:
            print("Number is not prime.")
            return
        if divisor > self.input // 2:
            print("Number is prime.")
        elif self.input % divisor == 0:
            print("Number is not prime.")
        else:
            self.primeNum(divisor + 1)


length = int(input("please enter list size: "))
user_input = []
for i in range(length):
    el = int(input("Please, enter the element: "))
    user_input.append(el)
rotations = int(input("Please, enter number of rotations: ")) % length
shift_left_test = RecursiveFunctions(user_input)
shift_left_test.leftshiftList(rotations)
print("Left shift: ", shift_left_test.input)
shift_left_test.refresh(user_input)
shift_left_test.rightshiftList(rotations)
print("Right shift: ", shift_left_test.input)
toggle_case_input = [char for char in input("Please, enter string you want to toggle case: ")]
shift_left_test = RecursiveFunctions(toggle_case_input)
shift_left_test.refresh(toggle_case_input)
shift_left_test.toggleCase()
print("Toggle case: ", "".join(shift_left_test.input))
perfect_num_input = int(input("Please, enter number to check if it's perfect: "))
shift_left_test = RecursiveFunctions(perfect_num_input)
shift_left_test.refresh(perfect_num_input)
shift_left_test.perfectNumber(0, 1)
prime_num_input = int(input("Please, enter number to check if it's prime: "))
shift_left_test.refresh(prime_num_input)
shift_left_test.primeNum(2)




