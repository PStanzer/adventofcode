from collections import Counter

file = open('input.txt', 'r')

lines = file.read().split("\n")
lines.pop()
#print(lines)
#print(len(lines))
print(len(lines[1]))

def find_xmas(str):
    return str.count("XMAS")

flipped=[]
for i in range(len(lines[0])):
    col=""
    for j in range(len(lines)):
        col+=lines[j][i]
    flipped.append(col)

#print(flipped)

diagonals1=[]
for i in range(0,len(lines)):
    dia=""
    dia_ob=""
    for j in range(0,len(lines)-i):
        dia+=lines[j+i][j]
        dia_ob+=lines[j][j+i]
    #print(i,j,dia)
    #print(i,j,dia_ob)
    diagonals1.append(dia)
    diagonals1.append(dia_ob)
    
diagonals1.pop(0)
#print(diagonals1)

#diagonals2=[]
#for i in range(0,len(flipped)):
#    dia=""
#    dia_ob=""
#    for j in range(0,len(flipped)-i):
#        dia+=flipped[j+i][j]
#        dia_ob+=flipped[j][j+i]
#    #print(i,j,dia)
#    #print(i,j,dia_ob)
#    diagonals2.append(dia)
#    diagonals2.append(dia_ob)

diagonals2=[]
for i in range(0,len(lines)):
    dia=""
    dia_ob=""
    for j in range(0,len(lines)-i):
        dia+=lines[i+j][len(lines)-1-j]
        dia_ob+=lines[j][len(lines)-1-i-j]
    #print(i,j,dia)
    #print(i,j,dia_ob)
    diagonals2.append(dia)
    diagonals2.append(dia_ob)
    
diagonals2.pop(0)
#print(diagonals2)

res=0
for line in lines:
    res+=find_xmas(line)
    res+=find_xmas(line[::-1])

print(res)
for fine in flipped:
    res+=find_xmas(fine)
    res+=find_xmas(fine[::-1])

print(res)
for diag in diagonals1:
    res+=find_xmas(diag)
    res+=find_xmas(diag[::-1])

print(res)
for diag2 in diagonals2:
    res+=find_xmas(diag2)
    res+=find_xmas(diag2[::-1])

print(res)