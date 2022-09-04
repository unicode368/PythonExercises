equation = input("Please enter equation: ")
push_parenthesis = ('(', '[', '{')
pop_parenthesis = (')', ']', '}')
operators = ('+', '-', '/', '*', '^')
check_stack = []
valid = True

for i in range(len(equation)):
    if equation[i] in push_parenthesis:
        check_stack.append(equation[i])
    elif equation[i] in pop_parenthesis:
        if pop_parenthesis.index(equation[i]) == push_parenthesis \
                .index(check_stack[len(check_stack) - 1]):
            check_stack.pop()
        else:
            break
    if i + 1 < len(equation):
        if equation[i] in operators and (equation[i + 1] in operators):
            valid = False
        elif equation[i].isalpha() and equation[i + 1].isalpha():
            valid = False
        elif equation[i].isalpha() and equation[i + 1] in push_parenthesis:
            valid = False
        elif equation[-1] in operators:
            valid = False
        elif equation[i] in pop_parenthesis and equation[i + 1].isalpha():
            valid = False
        elif equation[i] in operators and equation[i + 1] in pop_parenthesis:
            valid = False
            break
        if not valid:
            break


if len(check_stack) == 0 and valid:
    print("Equation is valid")
else:
    print("Equation is invalid")
