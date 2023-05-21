second, first = (int(x) for x in input().split())


first_set = set()
second_set = set()

for _ in range(1, first + 1):
    first_set.add(input())

for _ in range(1, second + 1):
    second_set.add(input())

print(*(first_set.intersection(second_set)), sep="\n")
