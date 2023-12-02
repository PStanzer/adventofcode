file1 = open('input.txt', 'r')
Lines = file1.readlines()
count=0
res=0
for line in Lines:
    count += 1
    maxred=0
    maxgreen=0
    maxblue=0
    temp=line.split(":",1)[1]
    for take in temp.split(';'):
        for pair in take.split(','):
            a=pair.strip().split()
            if a[1]=="red":
                if int(a[0])>int(maxred):
                    maxred=a[0]
            elif a[1]=="green":
                if int(a[0])>int(maxgreen):
                    maxgreen=a[0]
            elif a[1]=="blue":
                if int(a[0])>int(maxblue):
                    maxblue=a[0]
    power=int(maxred)*int(maxgreen)*int(maxblue)
    res+=power
print(res)