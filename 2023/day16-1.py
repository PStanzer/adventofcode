file1 = open('input.txt', 'r')
grid = file1.read().split("\n")

newbeams=[((88,len(grid)-1),(0,-1))]
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

for beam in newbeams:
    pos,dir=beam
    cache=0
    i=1
    while pos[0] >= 0 and pos[0] < len(grid[0]) and pos[1] >= 0 and pos[1] < len(grid):
        energized.append(pos)
        pos,dir=move(pos,dir)
        energized=list(set(energized))
        i+=1
        if i%10 == 0:
            if cache == len(energized):
                break
            else:
                cache=len(energized)

print(len(set(energized)))
