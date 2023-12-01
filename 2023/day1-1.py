file1 = open('./input/day1-1.txt', 'r')
Lines = file1.readlines()

count = 0
sum = 0
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
    for i, c1 in enumerate(line):
        if c1.isdigit():
            break
    for i, c2 in enumerate(reversed(line)):
        if c2.isdigit():
            break
    print(int(c1+c2))
    sum+=int(c1+c2)
    
print(sum)
