from collections import Counter

file = open('input.txt', 'r')

lines = file.read().split("\n")
lines.pop()

left=[]
right=[]
for line in lines:
    left.append(int(line.split()[0]))
    right.append(int(line.split()[1]))

sum=0
for l in left:
    sum+=l*right.count(l)

print(sum)
