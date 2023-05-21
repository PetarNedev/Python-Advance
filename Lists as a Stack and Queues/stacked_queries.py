lines = int(input())

my_stack = []

for _ in range(lines):
    numbers = [int(x) for x in input().split()]
    command = numbers[0]

    if command == 1:
        number = numbers[1]
        my_stack.append(number)
    elif command == 2:
        if my_stack:
            my_stack.pop()
    elif command == 3:
        if my_stack:
            print(max(my_stack))
    elif command == 4:
        if my_stack:
            print(min(my_stack))


print(*my_stack[::-1], sep=", ")


