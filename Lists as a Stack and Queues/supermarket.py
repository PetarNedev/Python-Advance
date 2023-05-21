from collections import deque

queue = deque()

while True:
    command = input()

    if command != "Paid":
        if command == "End":
            break
        queue.append(command)
    else:
        while queue:
            person = queue.popleft()
            print(person)
print(f"{len(queue)} people remaining.")
