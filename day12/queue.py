def enqueue():
    global rear
    if rear == max - 1:
        print("Queue overflow")
    else:
        ele = int(input("Enter ele = "))
        rear += 1
        a[rear] = ele


def dequeue():
    global front, rear
    if front > rear:
        print("Queue underflow")
    else:
        print("deleting  = ", a[front])
        a[front] = None
        front += 1


def display():
    if front > rear:
        print("Queue empty")
    else:
        for i in range(front, rear + 1):
            print(a[i], end=" --> ")
        print()


# main
front = 0
rear = -1
max = 5
a = [None] * max
while True:
    print("1 ENQUEUE 2 DEQUEUE 3 DISPLAY 4 EXIT")
    ch = int(input("Enter the choice  = "))
    if ch == 1:
        enqueue()
    elif ch == 2:
        dequeue()
    elif ch == 3:
        display()
    elif ch == 4:
        break
    else:
        print("Invalid choice ")
