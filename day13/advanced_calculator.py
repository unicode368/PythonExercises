exp = "+-8/632"[::-1]
stack = []

for i in range(len(exp)):
    if exp[i].isdigit():
        stack.append(exp[i])
    else:
        num1 = int(stack.pop())
        num2 = int(stack.pop())
        if exp[i] == "+":
            stack.append(num1 + num2)
        elif exp[i] == "-":
            stack.append(num1 - num2)
        elif exp[i] == "*":
            stack.append(num1 * num2)
        elif exp[i] == "/":
            stack.append(num1 / num2)
        elif exp[i] == "^":
            stack.append(num1**num2)

print(stack.pop())
