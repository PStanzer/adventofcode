file = open('input.txt', 'r')

lines = file.read().split("\n")
lines.pop()
print(lines)

def check_level(l):
    for i in range(len(l)-1):
        if abs(l[i]-l[i+1]) == 0:
            print("NULL")
            return False
        if abs(l[i]-l[i+1]) > 3:
            print("BIG")
            return False
    print("true")
    return True

def check_sort(l):
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
    if check_sort(l) and check_level(l):
        safe+=1
    else:
        for i in range(len(l)):
            print(i)
            nl=l.copy()
            nl.pop(i)
            print(nl)
            print(l)
            if check_sort(nl) and check_level(nl):
                safe+=1
                break
        

print(safe)