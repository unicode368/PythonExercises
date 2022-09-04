
def pop():
    global top, bottom
    if top == max and bottom == -1:
        print("Stack underflow")
    else:
        option = int(input("Select position: \n1 TOP \n2 BOTTOM"))
        while option != 1 and option != 2:
            option = int(input("Select position: \n1 TOP \n2 BOTTOM"))
        ele = int(input("Enter element"))
        if option == 1:
            if top == max:
                print("Stack underflow")
                return
            print("deleting .... = ", a[top])
            a[top] = ele
            top += 1
        else:
            if bottom == -1:
                print("Stack underflow")
                return
            print("deleting .... = ", a[bottom])
            a[bottom] = ele
            bottom -= 1


def display():
    global top
    if top == max and bottom == -1:
        print("Stack is empty")
    else:
        print("Elements of stack are = ")
        print("---")
        for i in range(max - 1, -1, -1):
            if bottom < i < top:
                print()
            else:
                print(a[i])
            print("---")


def peek():
    global top
    print("-------------------------------")
    print("Top most element = ",a[top])
    print("-------------------------------")


def bottom_el():
    global bottom
    print("-------------------------------")
    print("Bottom most element = ", a[bottom])
    print("-------------------------------")


def push():
    global top, bottom
    if top - 1 == bottom:
        print("Stack overflow")
    else:
        option = int(input("Select position: \n1 TOP \n2 BOTTOM\n"))
        while option != 1 and option != 2:
            option = int(input("Select position: \n1 TOP \n2 BOTTOM\n"))
        ele = int(input("Enter element"))
        if option == 1:
            top -= 1
            a[top] = ele
        else:
            bottom += 1
            a[bottom] = ele


max = 10
a = [0] * max
top = max
bottom = -1

while True:
    user_input = int(input("Select option: \n1 PUSH \n2 POP \n3 PEEK \n4 BOTTOM \n5 DISPLAY \n6 EXIT"))
    if user_input == 1:
        push()
    elif user_input == 2:
        pop()
    elif user_input == 3:
        peek()
    elif user_input == 4:
        bottom_el()
    elif user_input == 5:
        display()
    elif user_input == 6:
        break
    else:
        print("Invalid input")