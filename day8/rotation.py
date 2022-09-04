def display():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()


def generate_matrix(n):
    res = []
    row = []
    counter = 1
    for i in range(n):
        for j in range(n):
            row.append(counter)
            counter += 1
        res.append(row)
        row = []
    return res


size = int(input("Enter matrix size:"))
matrix = generate_matrix(size)

while True:
    n = int(input("Choose an option: \n1. Left rotate. \n2. Right rotate. \n3. Exit. \n"))
    if n == 3:
        break
    elif n == 2:
        times = int(input("How many times you want to rotate?"))
        while times > 0:
            for i in range(len(matrix)):
                for j in range(i, len(matrix[i])):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp

            for i in range(len(matrix)):
                for j in range(len(matrix[i]) // 2):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[i][len(matrix) - j - 1]
                    matrix[i][len(matrix) - j - 1] = temp
            times -= 1
    elif n == 1:
        times = int(input("How many times you want to rotate?"))
        while times > 0:
            for i in range(len(matrix)):
                for j in range(i, len(matrix[i])):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
            for j in range(len(matrix)):
                for i in range(len(matrix) // 2):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[len(matrix) - i - 1][j]
                    matrix[len(matrix) - i - 1][j] = temp
            times -= 1
    print("Matrix after rotation:\n")
    display()