file = open('input.txt', 'r')

lines = file.read().split("\n").pop()

floor: int = 0

for char in lines:
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
    else:
        print("wrong char")

print(floor)
