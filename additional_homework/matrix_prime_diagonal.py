"""
Write a Python program to read a square matrix from console and print the sum of matrix primary diagonal. 
Accept the size of the square matrix and elements for each column separated with a space (for every row) as input from the user. 
Input the size of the matrix: 3
2 3 4
4 5 6
3 4 7
Sum of matrix primary diagonal:
14
"""

matrix = []
matrix_size = input("How many rows does your matrix have? ")

for i in range(int(matrix_size)):
    matrix.append(input(f"Matrix row {i}: ").split(" "))

primary_diagonal = []
index = 0

while index < len(matrix):
    primary_diagonal.append(matrix[index][index])
    index += 1


sum = sum([int(x) for x in primary_diagonal])

print(sum)