file = open('input.txt', 'r')

lines = file.read().split("\n")
lines.pop()
print(lines)

def check1(l):
    for i in range(len(l)-1):
        if abs(l[i]-l[i+1]) == 0:
            print("NULL")
            return False
        if abs(l[i]-l[i+1]) > 3:
            print("BIG")
            return False
    print("true")
    return True

def check2(l):
    if l==sorted(l):
        print("sor")
        return True
    elif l==sorted(l, reverse=True):
        print("inv")
        return True
    else:
        print("NOT SOR")
        return False

safe=0
for line in lines:
    l=[int(c) for c in line.split(' ')]
    print(l)
    if check1(l) and check2(l):
        safe+=1

print(safe)