import itertools
from fractions import Fraction

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
    print("Positions:",list_0)

    combs=list(itertools.combinations(list_0,2))

    for comb in combs:
        dx=comb[0][0]-comb[1][0]
        dy=comb[0][1]-comb[1][1]
        #print(dx,dy)
        dx=Fraction(dx,dy).numerator
        dy=Fraction(dx,dy).denominator
        #print(dx,dy)
        
        
        pos1=[comb[0][0],comb[0][1]]
        if (pos1[0],pos1[1]) not in antinodes:
            antinodes.append((pos1[0],pos1[1]))
        while 0 <= pos1[0] < len(lines[0]) and 0 <= pos1[1] < len(lines):
            if (pos1[0],pos1[1]) not in antinodes:
                antinodes.append((pos1[0],pos1[1]))
            pos1[0]+=dx
            pos1[1]+=dy
        pos1=[comb[0][0],comb[0][1]]
        while 0 <= pos1[0] < len(lines[0]) and 0 <= pos1[1] < len(lines):
            if (pos1[0],pos1[1]) not in antinodes:
                antinodes.append((pos1[0],pos1[1]))
            pos1[0]-=dx
            pos1[1]-=dy

#        a1x=comb[0][0]+dx
#        a1y=comb[0][1]+dy
#        if 0 <= a1x < len(lines[0]) and 0 <= a1y < len(lines):
#            print("anti-1: ",comb[0][0]+dx,",",comb[0][1]+dy)
#            if (a1x,a1y) not in antinodes:
#                antinodes.append((a1x,a1y))
#        a2x=comb[1][0]-dx
#        a2y=comb[1][1]-dy
#        if 0 <= a2x < len(lines[0]) and 0 <= a2y < len(lines):
#            print("anti-2: ",comb[1][0]-dx,",",comb[1][1]-dy)
#            if (a2x,a2y) not in antinodes:
#                antinodes.append((a2x,a2y))

#check_char("0")
#check_char("A")

done=["."]
for line in lines:
    for c in line:
        if c not in done:
            print("starting with:",c)
            done.append(c)
            check_char(c)
#antinodes.sort()
#print(antinodes)
print(len(antinodes))
