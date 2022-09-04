exp = "K+L-M*N+(O^P)*W/U/V*T+Q"
# exp = "(a+(b-c+d)/e*f^g-(h/i-(j-(k*l)*m)^n)+p)"

priorities = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "{": 4, "(": 4, "[": 4,
              "]": 4, ")": 4, "}": 4, }
openingbrac = "{[("
closingbrac = "}])"
prefix = ""
operators = []
print(exp)

for i in range(len(exp)):
    if not exp[i].isalpha():
        if len(operators) > 0 and priorities[exp[i]] <= priorities[operators[-1]] \
                and operators[-1] not in openingbrac:
            while len(operators) > 0 and (priorities[exp[i]] <= priorities[operators[-1]]):
                if operators[-1] in openingbrac:
                    break
                prefix += operators[-1]
                operators.pop()
            operators.append(exp[i])
        elif exp[i] in closingbrac:
            while len(operators) > 0 and operators[-1] != openingbrac[closingbrac.index(exp[i])]:
                if operators[-1] not in openingbrac:
                    prefix += operators[-1]
                operators.pop()
            if len(operators) > 0:
                operators.pop()
        else:
            operators.append(exp[i])
    else:
        prefix += exp[i]
while len(operators) > 0:
    if operators[-1] not in closingbrac and operators[-1] not in openingbrac:
        prefix += operators[-1]
    operators.pop()
print("Result", prefix)