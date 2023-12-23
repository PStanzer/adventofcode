file1 = open('input.txt', 'r')
Lines = file1.read().split("\n")

for i,line in enumerate(Lines):
    if line.find('S') != -1:
        pos={(line.find('S'),i)}
        Lines[i]=Lines[i].replace('S','.')
        break

def step(positons):
    newpos=set()
    for pos in positons:
        if Lines[pos[1]-1][pos[0]] == '.':
            newpos=newpos.union({(pos[0],pos[1]-1)})
        if Lines[pos[1]+1][pos[0]] == '.':
            newpos=newpos.union({(pos[0],pos[1]+1)})
        if Lines[pos[1]][pos[0]-1] == '.':
            newpos=newpos.union({(pos[0]-1,pos[1])})
        if Lines[pos[1]][pos[0]+1] == '.':
            newpos=newpos.union({(pos[0]+1,pos[1])})
    return newpos

sol=set()
for i in range(1,65):
    pos=step(pos)
    if i%2 == 0:
        pos=pos.difference(sol)
        sol=sol.union(pos)

print(len(sol))
