from collections import Counter

file = open('input.txt', 'r')

lines = file.read().split("\n")
lines.pop()

def find_xmas(row,col):
    if (lines[row-1][col-1] == "M" and lines[row+1][col+1] == "S") or (lines[row-1][col-1] == "S" and lines[row+1][col+1] == "M"):
        if (lines[row+1][col-1] == "M" and lines[row-1][col+1] == "S") or (lines[row+1][col-1] == "S" and lines[row-1][col+1] == "M"):
            #print(row,col)
            return True
    else:
        return False

res=0
for i in range(1,len(lines)-1):
    for j in range(1,len(lines)-1):
        if lines[i][j] == "A":
            if find_xmas(i,j):
                res+=1
            
print(res)