file1 = open('input.txt', 'r')
grid = file1.read().split("\n")

newbeams=[((0,0),(0,1))]
energized=[]

def move(pos,dir):
    newpos=(pos[0]+dir[0],pos[1]+dir[1])
    if newpos[0] < 0 or newpos[0] >= len(grid[0]) or newpos[1] < 0 or newpos[1] >= len(grid):
        return newpos,dir
    match grid[newpos[1]][newpos[0]]:
        case '.':
            return newpos,dir
        case '|':
            if dir[1] == 0:
                if (newpos,(0,1)) in newbeams:
                    pass
                else:
                    newbeams.append((newpos,(0,1)))
                return newpos,(0,-1)
            else:
                return newpos,dir
        case '-':
            if dir[0] == 0:
                if (newpos,(1,0)) in newbeams:
                    pass
                else:
                    newbeams.append((newpos,(1,0)))
                return newpos,(-1,0)
            else:
                return newpos,dir
        case '/':
            if dir[0] == 1:
                return newpos,(0,-1)
            elif dir[0] == -1:
                return newpos,(0,1)
            if dir[1] == 1:
                return newpos,(-1,0)
            if dir[1] == -1:
                return newpos,(1,0)
        case '\\':
            if dir[0] == 1:
                return newpos,(0,1)
            elif dir[0] == -1:
                return newpos,(0,-1)
            if dir[1] == 1:
                return newpos,(1,0)
            if dir[1] == -1:
                return newpos,(-1,0)
    return newpos,dir

res=0
print('vertical left')
for j in range(len(grid)): #
    if grid[j][0] == '.':
        newbeams=[((0,j),(1,0))]
    else:
        newbeams=[]
        newbeams.append((move((-1,j),(1,0))))
    energized=[]
    cache=[]
    for beam in newbeams:
        pos,dir=beam
        i=1
        while pos[0] >= 0 and pos[0] < len(grid[0]) and pos[1] >= 0 and pos[1] < len(grid):
            energized.append(pos)
            cache.append((pos,dir))
            pos,dir=move(pos,dir)
            if (pos,dir) in cache:
                break
            energized=list(set(energized))
    if len(energized) > res:
        res=len(energized)

print('vertical right')
for j in range(len(grid)):
    if grid[j][-1] == '.':
        newbeams=[((len(grid)-1,j),(-1,0))]
    else:
        newbeams=[]
        newbeams.append((move((len(grid),j),(-1,0))))
    energized=[]
    cache=[]
    for beam in newbeams:
        pos,dir=beam
        i=1
        while pos[0] >= 0 and pos[0] < len(grid[0]) and pos[1] >= 0 and pos[1] < len(grid):
            energized.append(pos)
            cache.append((pos,dir))
            pos,dir=move(pos,dir)
            if (pos,dir) in cache:
                break
            energized=list(set(energized))
    if len(energized) > res:
        res=len(energized)

print('horizontal top')
for j in range(len(grid)):
    if grid[0][j] == '.':
        newbeams=[((j,0),(0,1))]
    else:
        newbeams=[]
        newbeams.append((move((j,-1),(0,1))))
    energized=[]
    cache=[]
    for beam in newbeams:
        pos,dir=beam
        i=1
        while pos[0] >= 0 and pos[0] < len(grid[0]) and pos[1] >= 0 and pos[1] < len(grid):
            energized.append(pos)
            cache.append((pos,dir))
            pos,dir=move(pos,dir)
            if (pos,dir) in cache:
                break
            energized=list(set(energized))
    if len(energized) > res:
        res=len(energized)

print('horizontal bottom')
for j in range(len(grid)):
    if grid[-1][j] == '.':
        newbeams=[((j,len(grid)-1),(0,-1))]
    else:
        newbeams=[]
        newbeams.append((move((j,len(grid)),(0,-1))))
    energized=[]
    cache=[]
    for beam in newbeams:
        pos,dir=beam
        i=1
        while pos[0] >= 0 and pos[0] < len(grid[0]) and pos[1] >= 0 and pos[1] < len(grid):
            energized.append(pos)
            cache.append((pos,dir))
            pos,dir=move(pos,dir)
            if (pos,dir) in cache:
                break
            energized=list(set(energized))
    if len(energized) > res:
        res=len(energized)

print(res)
