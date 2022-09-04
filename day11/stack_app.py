def push():
    global top
    if top == max - 1:
        print("Stack overflow")
    else:
        ele = int(input("Enter the ele = "))
        top += 1
        a[top] = ele


def pop():
    global top
    if top == -1:
        print("Stack underflow")
    else:
        print("deleting .... = ", a[top])
        top -= 1


def display():
    global top
    if top == -1:
        print("Stack is empty")
    else:
        print("Elements of stack are = ")
        for i in range(top, -1, -1):
            print(a[i])


def peek():
    global top
    print("-------------------------------")
    print("Top most element = ", a[top])
    print("-------------------------------")


max = 5
a = [0] * max
top = -1

while True:
    print("1 PUSH 2 POP 3 PEEK 4 DISPLAY 5 EXIT")
    ch = int(input("Enter the choice  = "))
    if ch == 1:
        push()
    elif ch == 2:
        pop()
    elif ch == 3:
        peek()
    elif ch == 4:
        display()
    elif ch == 5:
        break
    else:
        print("invalid choice")
