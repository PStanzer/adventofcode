file1 = open('input.txt', 'r')
Lines = file1.read().split("\n")

make_binary = lambda x:0 if x=='L' else 1
directions=[make_binary(x) for x in Lines[0]]
nodes={x.split('=')[0].strip():x.split('=')[1].strip().strip('()').split(', ') for x in Lines[2:]}

node='AAA'
i=0
res=0
while node != 'ZZZ':
    if i >= len(directions):
        i=0
    node=nodes[node][directions[i]]
    i+=1
    res+=1

print('res:',res)
    
