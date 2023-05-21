lines = int(input())
unique_elements = set()

for i in range(1, lines + 1):
    elements = input().split()
    for element in elements:
        unique_elements.add(element)

print(*unique_elements, sep="\n")
