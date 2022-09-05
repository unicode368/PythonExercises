class MatrixOperations:
    def set_dimension(self):
        self.rows = int(input("Enter rows = "))
        self.cols = int(input("Enter cols = "))
        self.matrix = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(0)
            self.matrix.append(row)

    def set_matrix(self):
        print("-------------------------------------")
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = int(input("Enter next element = "))
        return self.matrix

    def add2matrix(self, b):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] += b.matrix[i][j]

    def mul2matrix(self, b):
        self.matrixA = self.set_matrix()
        self.matrixB = b.set_matrix()
        c = []
        for i in range(self.rows):
            row = []
            for j in range(b.cols):
                el = 0
                for k in range(b.rows):
                    el += self.matrixA[i][k] * self.matrixB[k][j]
                row.append(el)
            c.append(row)
        self.res = c

    def display(self):
        for i in range(len(self.res)):
            for j in range(len(self.res[i])):
                print(self.matrix[i][j], end="\t")
            print()


a = MatrixOperations()
b = MatrixOperations()
a.set_dimension()
b.set_dimension()
a.mul2matrix(b)
a.display()

#a = MatrixOperations()
#a.set_dimension()
#a.set_matrix()
#b = MatrixOperations()
#b.set_dimension()
#b.set_matrix()

#a.add2matrix(b)
#a.display()

#a.add2matrix(b)
#a.display()
