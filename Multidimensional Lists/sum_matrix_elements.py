rows, cols = [int(el) for el in input().split(", ")]

matrix = []
sum_num = 0
for _ in range(rows):
    inner_list = [int(el) for el in input().split(", ")]
    sum_num += sum(inner_list)
    matrix.append(inner_list)

print(sum_num)
print(matrix)
