import random

class Matrix:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.matrix = []
        for i in range(self.row):
            newList = []
            for j in range(self.column):
                newList.append(random.randint(0,100))
            self.matrix.append(newList)
    
    def __str__(self):
        matrixStr = ""
        for i in range(self.row):
            for j in range(self.column):
                matrixStr += " " + str(self.matrix[i][j])
            matrixStr += "\n"
        return matrixStr
    
    def __add__(self, matrix2):
        if self.column == matrix2.column and self.row == matrix2.row:
            newMatrix = Matrix(self.row, self.column)
            for i in range(self.row):
                for j in range(self.column):
                    newMatrix.matrix[i][j] = self.matrix[i][j] + matrix2.matrix[i][j]
            return newMatrix
        else:
            raise Exception("Matrix sizes are different, can't apply addition operation!")

    def __sub__(self, matrix2):
        if self.column == matrix2.column and self.row == matrix2.row:
            newMatrix = Matrix(self.row, self.column)
            for i in range(self.row):
                for j in range(self.column):
                    newMatrix.matrix[i][j] = self.matrix[i][j] - matrix2.matrix[i][j]
            return newMatrix
        else:
            raise Exception("Matrix sizes are different, can't apply subtraction operation!")

    def __mul__(self, matrix2):
        if self.column == matrix2.row:
            newMatrix = Matrix(self.row, self.column)
            for i in range(self.row):
                for j in range(self.column):
                    sum = 0
                    for k in range(self.column):
                        sum += self.matrix[i][k] * matrix2.matrix[k][j]
                    newMatrix.matrix[i][j] = sum
            return newMatrix
        else:
            raise Exception("Incorrect matrix sizes, can't apply multiplication operation!")

ob1 = Matrix(3,3)
print(f"First object \n{ob1}")

ob2 = Matrix(3,3)
print(f"Second object \n{ob2}")

try:
    #print(f"Addition operation applied.\n{ob1.addition(ob2)}")
    print(f"Addition operation applied.\n{ob1+ob2}")
except Exception as e:
    print(e)
try:
    #print(f"Subtraction operation applied.\n{ob1.subtraction(ob2)}")
    print(f"Subtraction operation applied.\n{ob1-ob2}")
except Exception as e:
    print(e)
try:
    #print(f"multiplication operation applied.\n{ob1.multiplication(ob2)}")
    print(f"multiplication operation applied.\n{ob1*ob2}")
except Exception as e:
    print(e)
