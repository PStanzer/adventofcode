file = open('input.txt', 'r')

lines = file.read().split("\n")
lines.pop()
print(lines)

start=()
for i,line in enumerate(lines):
    s=line.find("^")
    if s > 0:
        print(i, s)
        start=(i,s)

print(lines[6][4])

pos=start
#match lines[6][4]:
#    case "^":
#        dir="up"
#    case ">":
#        dir="right"
#    case "v":
#        dir="down"
#    case "<":
#        dir="left"
dir="up"
print(pos,dir)
exit
visited=[pos]
def move(p,d):
    match d:
        case "up":
            if lines[p[0]-1][p[1]] == "#":
                print("stop")
                d="right"
                return p,d
            else:
                p=(p[0]-1,p[1])
        case "right":
            if lines[p[0]][p[1]+1] == "#":
                print("stop")
                d="down"
                return p,d
            else:
                p=(p[0],p[1]+1)
        case "down":
            if lines[p[0]+1][p[1]] == "#":
                print("stop")
                d="left"
                return p,d
            else:
                p=(p[0]+1,p[1])
        case "left":
            if lines[p[0]][p[1]-1] == "#":
                print("stop")
                d="up"
                return p,d
            else:
                p=(p[0],p[1]-1)
    #print(p,d)
    if p not in visited:
        visited.append(p)
    return p,d

while 1:
    #print(visited)
    print("len",len(visited))
    pos,dir=move(pos,dir)
    