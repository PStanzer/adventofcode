file = open('input.txt', 'r')

lines = file.read().split("\n")

boxes = [line.split("x") for line in lines]

print(boxes)

paper_needed: int = 0

for box in boxes:
    if len(box) != 3:
        print("Box not defined")
        break
    side1: int = int(box[0])*int(box[1])
    side2: int = int(box[0])*int(box[2])
    side3: int = int(box[1])*int(box[2])
    paper_needed += 2*(side1+side2+side3) + min(side1,side2,side3)

print(paper_needed)