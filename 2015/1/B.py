file = open('input.txt', 'r')

lines = file.read().split("\n").pop()

floor: int = 0

for i,char in enumerate(lines):
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
    else:
        print("wrong char")
    if floor == -1:
        print(i+1)
        break
