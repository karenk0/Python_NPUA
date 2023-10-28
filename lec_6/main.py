import random

def generate_random_matrix(rows, cols):
    matrix = []
    for row in range(rows):
        list = []
        for column in range(cols):
            list.append(random.randint(1,100))
        matrix.append(list)
        print(list,"\n")
    return matrix

def get_column_sum(matrix, column_index):
    sum = 0
    for row, value in enumerate(matrix):
        sum += value[column_index]
    return sum

def get_row_average(matrix, row_index):
    mean = 0
    for column, value in enumerate(matrix[row_index]):
        mean += value
    mean /= len(matrix[row_index])
    return mean

rows = int(input("Input rows:   "))
columns = int(input("Input cols:   "))

matrix = generate_random_matrix(rows, columns)

rows = int(input("Input the row index, to calculate the mean of it's elements:   "))
columns = int(input("Input the column's index to calculate the sum of elements:   "))

mean = get_row_average(matrix, rows)
print(f"Mean of {rows}th row is {mean}")

sum = get_column_sum(matrix, columns)
print(f"Sum of {columns}th column is {sum}")
