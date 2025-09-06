file = open('input.txt', 'r')

lines = file.read().split("\n")

boxes = [line.split("x") for line in lines]

print(boxes)

ribbon_needed: int = 0

for box in boxes:
    if len(box) != 3:
        print("Box not defined")
        break
    circ1: int = 2*(int(box[0])+int(box[1]))
    circ2: int = 2*(int(box[0])+int(box[2]))
    circ3: int = 2*(int(box[1])+int(box[2]))
    volume: int = int(box[0])*int(box[1])*int(box[2])
    ribbon_needed += volume + min(circ1,circ2,circ3)

print(ribbon_needed)
    