file = open('input.txt', 'r')

lines = file.read().split("\n")
lines.pop()
#print(lines)

def move(p,d):
    match d:
        case "up":
            if grid[p[0]-1][p[1]] == "#":
                #print("stop")
                d="right"
                return p,d
            else:
                p=(p[0]-1,p[1])
        case "right":
            if grid[p[0]][p[1]+1] == "#":
                #print("stop")
                d="down"
                return p,d
            else:
                p=(p[0],p[1]+1)
        case "down":
            if grid[p[0]+1][p[1]] == "#":
                #print("stop")
                d="left"
                return p,d
            else:
                p=(p[0]+1,p[1])
        case "left":
            if grid[p[0]][p[1]-1] == "#":
                #print("stop")
                d="up"
                return p,d
            else:
                p=(p[0],p[1]-1)
    return p,d

start=()
for i,line in enumerate(lines):
    s=line.find("^")
    if s > 0:
        print(i, s)
        start=(i,s)

pos=start
dir="up"
path=[pos]

print(len(lines[0]))

while 1:
    grid=lines.copy()
    pos,dir=move(pos,dir)
    if pos not in path:
        path.append(pos)
        #print("len",len(path))
    if pos[0] == 0 and dir == "up":
        break
    if pos[1] == 0 and dir == "left":
        break
    if pos[0] == len(lines[0])-1 and dir == "down":
        break
    if pos[1] == len(lines[0])-1 and dir == "right":
        break
path.pop(0)
print(path)
print(lines)
count=0
for place in path:
    grid=lines.copy()
    grid[place[0]]=grid[place[0]][:place[1]]+"#"+grid[place[0]][place[1]+1:]
    print(grid)
    pos=start
    dir="up"
    new_path=[]
    while 1:
        pos,dir=move(pos,dir)
        if (pos,dir) in new_path:
            count+=1
            break
        else:
            new_path.append((pos,dir))
        if pos[0] == 0 and dir == "up":
            break
        if pos[1] == 0 and dir == "left":
            break
        if pos[0] == len(lines[0])-1 and dir == "down":
            break
        if pos[1] == len(lines[0])-1 and dir == "right":
            break
print(count)
print(lines)

