import re

f = open("input.txt", "r")
lines=f.read().split("do()")
#print(lines)
#lines=re.split("do\(\)",lines)
#print(len(lines))

res=0
for line in lines:
    #print(line.split("don't()")[0])
    out=re.findall("mul\(\d{1,3},\d{1,3}\)",line.split("don't()")[0])
    for call in out:
        mul=call.replace("mul(","").replace(")","").split(",")
        #print(mul)
        res+=int(mul[0])*int(mul[1])

#print(lines)
#print(out)
print(res)
