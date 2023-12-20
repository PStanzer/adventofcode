file1 = open('input.txt', 'r')
Lines = file1.read().split("\n")

# dirs are given like (y,x)
dirs = [(0,int(line.split()[1])) if line.split()[0] == 'R' else (0,-int(line.split()[1])) if line.split()[0] == 'L' else  (int(line.split()[1]),0) if line.split()[0] == 'D' else  (-int(line.split()[1]),0) for line in Lines]

def dig(pos,dir):
    for d in range(1,abs(dir[0])+1):
        if dir[0] < 0:
            boundary.append((pos[0]-d,pos[1],'u'))
        else:
            boundary.append((pos[0]+d,pos[1],'d'))
    for d in range(1,abs(dir[1])+1):
        if dir[1] < 0:
            boundary.append((pos[0],pos[1]-d,'h'))
        else:
            boundary.append((pos[0],pos[1]+d,'h'))
    newpos=(pos[0]+dir[0],pos[1]+dir[1])
    return newpos

corners=[[0,0],[0,0]] #(lowest y, lowest x), (biggest y biggest x)
boundary=[]
pos=(0,0)
for a,dir in enumerate(dirs):
    if a!=0:
        if dir[0] > 0:
            boundary.pop()
            boundary.append((pos[0],pos[1],'d'))
        elif dir[0] < 0:
            boundary.pop()
            boundary.append((pos[0],pos[1],'u'))
    pos=dig(pos,dir)
    if pos[0] < corners[0][0]:
        corners[0][0] = pos[0]
    if pos[0] > corners[1][0]:
        corners[1][0] = pos[0]
    if pos[1] < corners[0][1]:
        corners[0][1] = pos[1]
    if pos[1] > corners[1][1]:
        corners[1][1] = pos[1]

boundary=set(boundary)
pit=0
for i in range(corners[0][0]+1,corners[1][0],1):
    bdry=0
    prev=''
    for j in range(corners[0][1],corners[1][1],1):
        if (i,j,'u') in boundary and prev != 'u':
                bdry+=1
                prev='u'
        elif (i,j,'d') in boundary and prev != 'd':
                bdry-=1
                prev='d'
        elif (i,j,'h') in boundary:
                pass
        if (i,j,'u') in boundary or (i,j,'d') in boundary or (i,j,'h') in boundary:
            pass
        elif bdry != 0 and bdry % 2 == 1:
            pit+=1

print(pit+len(boundary))

# visual=[]
# for i in range(corners[0][0],corners[1][0]+1,1):
#     str=''
#     for j in range(corners[0][1],corners[1][1]+1,1):
#         if [i,j,'u'] in boundary or [i,j,'d'] in boundary or [i,j,'h'] in boundary:
#             str+='#'
#         elif (i,j) in pit:
#             str+='O'
#         else:
#             str+='.'
#     print(str)
