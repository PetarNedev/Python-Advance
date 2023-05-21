from collections import deque

names = deque(input().split())
rotation_number = int(input())

while len(names) > 1:
    names.rotate(-rotation_number)
    exit_name = names.pop()
    print(f"Removed {exit_name}")

print(f"Last is {names.pop()}")
