from collections import defaultdict

file1 = open('input.txt', 'r')
Lines = file1.read().split(',')

boxes=defaultdict(list)
for s in Lines:
    cur_val=0
    for c in s:
        if c == '-':
            boxes[cur_val]=[x for x in boxes[cur_val] if x.split()[0] != s.strip('-')]
            break
        elif c == '=':
            if len(boxes[cur_val]) == 0:
                boxes[cur_val].append(s.replace('=',' '))
            else:
                rep=False
                for i,lens in enumerate(boxes[cur_val]):
                    if s.split('=')[0] == lens.split()[0]:
                        boxes[cur_val][i]=s.replace('=',' ')
                        rep=True
                        break
                if not rep:
                    boxes[cur_val].append(s.replace('=',' '))
            break
        else:
            cur_val=((cur_val+ord(c))*17)%256

res=0
for i in range(256):
    for j,lens in enumerate(boxes[i]):
        res+=(i+1)*(j+1)*int(lens.split()[1])

print(res)
    