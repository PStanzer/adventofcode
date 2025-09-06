file = open('input.txt', 'r')

lines = file.read().split("\n")
lines.pop()
#print(lines)

newfs=[]
for i,c in enumerate(lines[0]):
    #print(c)
    if int(c) == 0:
        continue
    elif i % 2:
        newfs.append(["." for j in range(int(c))])
    else:
        newfs.append([str(int(i/2)) for j in range(int(c))])
        
#print(newfs)

j=len(newfs)
while True:
    block=newfs[j-1]
    #print(j,block)
    if "." not in block:
        for k,space in enumerate(newfs):
            #print(space)
            if "." in space and len(space) == len(block):
                #print(newfs[k],"repl",space,"with",block)
                newfs[k]=newfs[j-1]
                newfs[j-1]=["." for j in range(len(block))]
                #print(newfs[k])
                break
            elif "." in space and len(space) > len(block):
                #print("repl",space,"with",block,"and something")
                newfs[k]=newfs[j-1]
                newfs[j-1]=["." for j in range(len(block))]
                newfs.insert(k+1,["." for j in range(len(space)-len(block))])
                j+=1
                break
            elif k==j-1:
                print(newfs[k],"not repl",space,"with",block)
                break
    #print(newfs)
    j-=1
    if j==0:
        break
        
nfs=[]
for l in newfs:
    nfs+=l
#print(nfs)
res=0
for n,dig in enumerate(nfs):
    if dig!=".":
        #print(dig)
        res+=int(dig)*n
print(res)