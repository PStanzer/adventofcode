file1 = open('input.txt', 'r')
Lines = file1.read().split("\n")

for i, line in enumerate(Lines):
    if not line.find('S') == -1:
        start=[i,line.find('S')]
        break

dir=[]
match Lines[start[0]][start[1]+1]:
    case '-' | 'J' | '7':
        dir.append('east')
match Lines[start[0]+1][start[1]]:
    case '|' | 'L' | 'J':
        dir.append('south')
match Lines[start[0]][start[1]-1]:
    case '-' | 'L' | 'F':
        dir.append('west')
match Lines[start[0]-1][start[1]]:
    case '|' | '7' | 'F':
        dir.append('north')

def go(pos,dir):
    match dir:
        case 'east':
            newpos=[pos[0],pos[1]+1]
        case 'south':
            newpos=[pos[0]+1,pos[1]]
        case 'west':
            newpos=[pos[0],pos[1]-1]
        case 'north':
            newpos=[pos[0]-1,pos[1]]
    match Lines[newpos[0]][newpos[1]]:
        case '|':
            if dir == 'south':
                newdir='south'
            elif dir == 'north':
                newdir='north'
            else:
                print('ERROR')
        case '-':
            if dir == 'east':
                newdir='east'
            elif dir == 'west':
                newdir='west'
            else:
                print('ERROR')
        case 'L':
            if dir == 'south':
                newdir='east'
            elif dir == 'west':
                newdir='north'
            else:
                print('ERROR')
        case 'J':
            if dir == 'east':
                newdir='north'
            elif dir == 'south':
                newdir='west'
            else:
                print('ERROR')
        case '7':
            if dir == 'east':
                newdir='south'
            elif dir == 'north':
                newdir='west'
            else:
                print('ERROR')
        case 'F':
            if dir == 'west':
                newdir='south'
            elif dir == 'north':
                newdir='east'
            else:
                print('ERROR')
    #print(Lines[newpos[0]][newpos[1]],newpos,newdir)
    return (newpos, newdir)

                
pos1, dir1=go(start,dir[0])
pos2, dir2=go(start,dir[1])
cnt=1

while pos1!=pos2:
    pos1, dir1=go(pos1,dir1)
    pos2, dir2=go(pos2,dir2)
    cnt+=1

print(cnt)
print(pos1)
print(pos2)
