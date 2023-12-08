file1 = open('input.txt', 'r')
Lines = file1.read().split("\n")

make_binary = lambda x:0 if x=='L' else 1
directions=[make_binary(x) for x in Lines[0]]
nodes={x.split('=')[0].strip():x.split('=')[1].strip().strip('()').split(', ') for x in Lines[2:]}

check_start = lambda x: x if x[2]=='A' else None
start=[check_start(x.split('=')[0].strip()) for x in Lines[2:] if check_start(x.split('=')[0].strip()) is not None]
print(start)
check_finish = lambda x: True if x[2]=='Z' else False

i=0
res=0
#print(['A' for x in range(len(start))])
#print(check_node(start[0],'A'))
current=start
while 1:
#    print(i)
    if i >= len(directions):
#        break
        i=0
    current=[nodes[node][directions[i]] for node in current]
    print(current)
    i+=1
    res+=1
    print(res)
    if False in list(map(check_finish,current)):
        continue
    else:
        break

print('res:',res)
    
