file = open('input.txt', 'r')

lines = file.read().split("\n")
lines.pop()
print(lines)

left=[]
right=[]
for line in lines:
    left.append(int(line.split()[0]))
    right.append(int(line.split()[1]))

    print(left)
    print(right)

left.sort()
right.sort()

print(left)
print(right)

sum=0
for i,l in enumerate(left):
    sum+=abs(l-right[i])
    print(sum)

print(sum)
