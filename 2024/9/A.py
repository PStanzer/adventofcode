file = open('input.txt', 'r')

lines = file.read().split("\n")
lines.pop()
#print(lines)

newfs=[]
for i,c in enumerate(lines[0]):
    #print(c)
    for j in range(int(c)):
        if i % 2:
            newfs.append("")
        else:
            newfs.append(int(i/2))
        
print(len(newfs))

for k,c in enumerate(newfs):
    if c == "":
        newfs[k]=newfs.pop()
    while newfs[-1]=="":
        newfs.pop()
        
#print(newfs)

res=0
for n,dig in enumerate(newfs):
    res+=int(dig)*n
print(res)