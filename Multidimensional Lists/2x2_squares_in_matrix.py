rows, cols = [int(i) for i in input().split()]
matrix = [input(). split() for row in range(rows)]

match = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row+1][col] == matrix[row][col+1] == matrix[row+1][col+1]:
            match += 1

print(match)
