rows = int(input())

matrix = [[int(x) for x in input().split()]for row in range(rows)]
primary_diagonal = [matrix[index][index] for index in range(rows)]
secondary_diagonal = [matrix[index][rows - index - 1] for index in range(rows)]

primary_sum = sum(primary_diagonal)
secondary_sum = sum(secondary_diagonal)

print(abs(primary_sum - secondary_sum))
