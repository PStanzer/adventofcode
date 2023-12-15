file1 = open('sample.txt', 'r')
Lines = file1.read().split(',')

print(Lines)
res=0
for s in Lines:
    cur_val=0
    for c in s:
        cur_val=((cur_val+ord(c))*17)%256
    res+=cur_val
print(res)
