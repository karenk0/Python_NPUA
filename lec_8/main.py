import random

class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = []
        for i in range(self.n):
            row = []
            for j in range(self.m):
                row.append(random.randint(0,100))
            self.matrix.append(row)
    
    def printMatrix(self):
        for i in range(self.n):
            for j in range(self.m):
                print(f"{self.matrix[i][j]:3}", end=" ") #print matrix formatted
            print()
    
    def calculateMean(self):
        sum = 0
        for i in range(self.n):
            for j in range(self.m):
                sum += self.matrix[i][j]
        return sum // (self.m * self.n)

    def sumOfGivenRow(self, row):
        sum = 0
        for j in range(self.m):
            sum += self.matrix[row][j]
        return sum
    
    def averageOfGivenColumn(self, column):
        sum = 0
        for i in range(self.n):
            sum += self.matrix[i][column]
        return sum / self.n

    def printSubmatrix(self, col1, col2, row1, row2):       
        while row1 <= row2: 
            temp = col1
            while temp <= col2:
                print(f"{self.matrix[row1][temp]:3}", end=" ")
                temp += 1
            row1 += 1
            print()

matrixOb1 = Matrix(5,5)
matrixOb1.printMatrix()
print("Mean of matrix elements: ",matrixOb1.calculateMean())
columnAvgNumber = 1
print(f"Average of {columnAvgNumber} column: ", matrixOb1.averageOfGivenColumn(columnAvgNumber))
rowSumNumber = 0
print(f"Sum of {rowSumNumber} row: ", matrixOb1.sumOfGivenRow(rowSumNumber))
print("\nPrinting submatrix: ")
matrixOb1.printSubmatrix(1,3,0,3)
    
