matrix = [[1, 2, 3, 4, 5], [5, 6, 7, 8, 1], [6, 5, 4, 3, 7], [9, 8, 1, 17, 3], [8, 7, 6, 5, 4]]


def print_matrx():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()


shift = 0
print("Init val:")
print_matrx()
print("Result:")
for j in range(len(matrix) - 1):
    for i in range(j + 1, len(matrix)):
        temp = matrix[i][j]
        matrix[i][j] = matrix[shift][len(matrix[0]) - j - 1]
        matrix[shift][len(matrix[0]) - j - 1] = temp
        shift += 1
    shift = 0

print_matrx()
print()
