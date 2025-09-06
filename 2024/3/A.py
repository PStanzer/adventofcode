import re

f = open("input.txt", "r")
lines=f.read()

out=re.findall("mul\(\d{1,3},\d{1,3}\)",lines)
res=0
for call in out:
     mul=call.replace("mul(","").replace(")","").split(",")
#    print(mul)
     res+=int(mul[0])*int(mul[1])

#print(lines)
#print(out)
print(res)
