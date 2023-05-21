from collections import deque

parenthesis = deque(input())#{[(])}
open_parenthesis = deque()

while parenthesis:
    current_parenthesis = parenthesis.popleft()

    if current_parenthesis in "({[":
        open_parenthesis.append(current_parenthesis)
    elif not open_parenthesis:
        print("NO")
        break
    else:
        first_part = open_parenthesis.pop()
        second_part = current_parenthesis
        if f"{first_part + second_part}" not in "()[]{}":
            print("NO")
            break
else:
    print("YES")
