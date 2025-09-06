import itertools

file = open('input.txt', 'r')

lines = file.read().split("\n")
lines.pop()
print(lines)

antinodes=[]

def check_char(ch):
    list_0=[]
    for y,line in enumerate(lines):
        x=line.find(ch)
        if x != -1:
            list_0.append((x,y))
    print(list_0)

    combs=list(itertools.combinations(list_0,2))

    for comb in combs:
        dx=comb[0][0]-comb[1][0]
        dy=comb[0][1]-comb[1][1]
        a1x=comb[0][0]+dx
        a1y=comb[0][1]+dy
        if 0 <= a1x < len(lines[0]) and 0 <= a1y < len(lines):
            print("anti-1: ",comb[0][0]+dx,",",comb[0][1]+dy)
            if (a1x,a1y) not in antinodes:
                antinodes.append((a1x,a1y))
        a2x=comb[1][0]-dx
        a2y=comb[1][1]-dy
        if 0 <= a2x < len(lines[0]) and 0 <= a2y < len(lines):
            print("anti-2: ",comb[1][0]-dx,",",comb[1][1]-dy)
            if (a2x,a2y) not in antinodes:
                antinodes.append((a2x,a2y))

#check_char("0")
#check_char("A")

done=["."]
for line in lines:
    for c in line:
        if c not in done:
            done.append(c)
            check_char(c)
            print(c)

print(len(antinodes))
