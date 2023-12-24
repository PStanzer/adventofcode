import shapely
from shapely.geometry import LineString, Point

file1 = open('input.txt', 'r')
Lines = file1.read().split("\n")

lower=200000000000000
upper=400000000000000
trajs=[]
for line in Lines:
    pos, vel = line.split(' @ ')
    pos=pos.split(', ')
    vel=vel.split(', ')
    A=(lower,int(pos[1]) + ( lower-int(pos[0]) ) / int(vel[0]) * int(vel[1]))
    B=(upper,int(pos[1]) + ( upper-int(pos[0]) ) / int(vel[0]) * int(vel[1]))
    trajs.append(LineString([A,B]))

print(len(trajs))
ints=[]
for i,t in enumerate(trajs):
    for j in range(i+1,len(trajs)):
        print('i',i,'j',j)
        intersect=trajs[i].intersection(trajs[j])
        if intersect != LineString():
            if intersect.x > int(Lines[i].split(', ')[0]) and int(Lines[i].split(', ')[2].split(' @ ')[1]) < 0:
                continue
            if intersect.x < int(Lines[i].split(', ')[0])and int(Lines[i].split(', ')[2].split(' @ ')[1]) > 0:
                continue
            if intersect.y > int(Lines[i].split(', ')[1]) and int(Lines[i].split(', ')[3]) < 0:
                continue
            if intersect.y < int(Lines[i].split(', ')[1]) and int(Lines[i].split(', ')[3]) > 0:
                continue
            if intersect.x > int(Lines[j].split(', ')[0]) and int(Lines[j].split(', ')[2].split(' @ ')[1]) < 0:
                continue
            if intersect.x < int(Lines[j].split(', ')[0])and int(Lines[j].split(', ')[2].split(' @ ')[1]) > 0:
                continue
            if intersect.y > int(Lines[j].split(', ')[1]) and int(Lines[j].split(', ')[3]) < 0:
                continue
            if intersect.y < int(Lines[j].split(', ')[1]) and int(Lines[j].split(', ')[3]) > 0:
                continue
            if intersect.x < lower or intersect.x > upper or intersect.y < lower or intersect.y > upper:
                continue
            ints.append(intersect)

print(len(ints))
