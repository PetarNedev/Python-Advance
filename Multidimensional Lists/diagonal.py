rows = int(input())
matrix = [[int(x) for x in input().split(", ")]for row in range(rows)]
primary_diagonal = [matrix[index][index] for index in range(rows)]
secondary_diagonal = [matrix[index][rows - index - 1] for index in range(rows)]

print(f"Primary diagonal: {', '.join([str(el) for el in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(el) for el in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
