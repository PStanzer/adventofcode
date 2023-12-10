import sys
import numpy as np
np.set_printoptions(threshold=np.inf, edgeitems=None, linewidth=None, suppress=None)

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

def go(pos,dir,path):
    match dir:
        case 'east':
            newpos=[pos[0],pos[1]+1]
            if path==1:
                right.append((newpos[0]+1,newpos[1]))
            else:
                left.append((newpos[0]-1,newpos[1]))
        case 'south':
            newpos=[pos[0]+1,pos[1]]
            if path==1:
                right.append((newpos[0],newpos[1]-1))
            else:
                left.append((newpos[0],newpos[1]+1))
        case 'west':
            newpos=[pos[0],pos[1]-1]
            if path==1:
                right.append((newpos[0]-1,newpos[1]))
            else:
                left.append((newpos[0]+1,newpos[1]))
        case 'north':
            newpos=[pos[0]-1,pos[1]]
            if path==1:
                right.append((newpos[0],newpos[1]+1))
            else:
                left.append((newpos[0],newpos[1]-1))
    match Lines[newpos[0]][newpos[1]]:
        case '|':
            if dir == 'south':
                newdir='south'
                if path==1:
                    right.append((newpos[0],newpos[1]-1))
                else:
                    left.append((newpos[0]-1,newpos[1]+1))
            elif dir == 'north':
                newdir='north'
                if path==1:
                    right.append((newpos[0],newpos[1]+1))
                else:
                    left.append((newpos[0]-1,newpos[1]-1))
            else:
                print('ERROR')
        case '-':
            if dir == 'east':
                newdir='east'
                if path==1:
                    right.append((newpos[0]+1,newpos[1]))
                else:
                    left.append((newpos[0]-1,newpos[1]))
            elif dir == 'west':
                newdir='west'
                if path==1:
                    right.append((newpos[0]-1,newpos[1]))
                else:
                    left.append((newpos[0]+1,newpos[1]))
            else:
                print('ERROR')
        case 'L':
            if dir == 'south':
                newdir='east'
                if path==1:
                    right.append((newpos[0],newpos[1]-1))
                    right.append((newpos[0]+1,newpos[1]-1))
                    right.append((newpos[0]+1,newpos[1]))
            elif dir == 'west':
                newdir='north'
                if path==2:
                    left.append((newpos[0],newpos[1]-1))
                    left.append((newpos[0]+1,newpos[1]-1))
                    left.append((newpos[0]+1,newpos[1]))
            else:
                print('ERROR')
        case 'J':
            if dir == 'east':
                newdir='north'
                if path==1:
                    right.append((newpos[0],newpos[1]+1))
                    right.append((newpos[0]+1,newpos[1]+1))
                    right.append((newpos[0]+1,newpos[1]))
            elif dir == 'south':
                newdir='west'
                if path==2:
                    left.append((newpos[0],newpos[1]+1))
                    left.append((newpos[0]+1,newpos[1]+1))
                    left.append((newpos[0]+1,newpos[1]))
            else:
                print('ERROR')
        case '7':
            if dir == 'east':
                newdir='south'
                if path==2:
                    left.append((newpos[0],newpos[1]+1))
                    left.append((newpos[0]-1,newpos[1]+1))
                    left.append((newpos[0]-1,newpos[1]))
            elif dir == 'north':
                newdir='west'
                if path==1:
                    right.append((newpos[0],newpos[1]+1))
                    right.append((newpos[0]-1,newpos[1]+1))
                    right.append((newpos[0]-1,newpos[1]))
            else:
                print('ERROR')
        case 'F':
            if dir == 'west':
                newdir='south'
                if path==1:
                    right.append((newpos[0],newpos[1]-1))
                    right.append((newpos[0]-1,newpos[1]-1))
                    right.append((newpos[0]-1,newpos[1]))
            elif dir == 'north':
                newdir='east'
                if path==2:
                    left.append((newpos[0],newpos[1]-1))
                    left.append((newpos[0]-1,newpos[1]-1))
                    left.append((newpos[0]-1,newpos[1]))
            else:
                print('ERROR')
    #print(Lines[newpos[0]][newpos[1]],newpos,newdir)
    return (newpos, newdir)
    
right=[]
left=[]

pos1, dir1=go(start,dir[0],2)
pos2, dir2=go(start,dir[1],1)
cnt=1
pipes=[tuple(start),tuple(pos1),tuple(pos2)]
while pos1!=pos2:
    pos1, dir1=go(pos1,dir1,2)
    pos2, dir2=go(pos2,dir2,1)
    pipes.append(tuple(pos1))
    pipes.append(tuple(pos2))
    cnt+=1

fields=[x for x in set(right+left) if not x in pipes and not -1 in x]

# not the full general solution
print('sol',len(fields))

# generate an array with the whole map and mark all "next to pipe" fields
sol=np.zeros((len(Lines),len(Lines[0])))
for x in fields:
    sol[x[0]-1][x[1]-1]='5'

# print the map to find areas with undetected interior space
print(sol)
# fill the interior manually and count again!
