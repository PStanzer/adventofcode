import numpy as np

file1 = open('input.txt', 'r')
Lines = file1.read().split("\n")

make_binary = lambda x:0 if x=='L' else 1
directions=[make_binary(x) for x in Lines[0]]
nodes={x.split('=')[0].strip():x.split('=')[1].strip().strip('()').split(', ') for x in Lines[2:]}

check_start = lambda x: x if x[2]=='A' else None
current=[check_start(x.split('=')[0].strip()) for x in Lines[2:] if check_start(x.split('=')[0].strip()) is not None]

check_finish = lambda x: True if x[2]=='Z' else False

i=0
cnt=0
res=[0,0,0,0,0,0]
while 1:
    if i >= len(directions):
        i=0
    current=[nodes[node][directions[i]] for node in current]
    i+=1
    cnt+=1
    test=list(map(check_finish,current))
    if True in test:
        res[test.index(True)]=cnt
    if 0 not in res:
        break

print(np.lcm.reduce(res))
