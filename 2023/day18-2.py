file1 = open('input.txt', 'r')
Lines = file1.read().split("\n")

# dirs are given like (y,x)
dirs = [(0,int(line.split()[2].strip('(#)')[:-1],16)) if line.split()[2].strip('(#)')[-1] == '0' else (0,-int(line.split()[2].strip('(#)')[:-1],16)) if line.split()[2].strip('(#)')[-1] == '2' else  (int(line.split()[2].strip('(#)')[:-1],16),0) if line.split()[2].strip('(#)')[-1] == '1' else  (-int(line.split()[2].strip('(#)')[:-1],16),0) for line in Lines]

x=[0]
y=[0]
boundary=0
for dir in dirs:
    x.append((x[-1]+dir[1]))
    y.append((y[-1]+dir[0]))
    boundary+=abs(dir[0]+dir[1])

A=0
for i in range(1,len(x)):
    A+=(y[i-1]+y[i])*(x[i-1]-x[i])
A+=(y[-1]+y[0])*(x[-1]-x[0])

print(int(A/2)+boundary/2+1)
