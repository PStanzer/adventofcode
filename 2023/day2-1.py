file1 = open('input.txt', 'r')
Lines = file1.readlines()
count=0
res=0
for line in Lines:
    possible="true"
    count += 1
    color="none"
    for w in line.split():
        if color != "none":
            found=color.find(w.strip(',;'))
            if found == 0 or found == 5:
                color="none"
            else:
                possible="false"
                break
        if w.isdigit():
            if int(w) > 14:
                possible="false"
                break
            elif int(w) == 14:
                color="blue"
            elif int(w) == 13:
                color="blue green"
            else:
                color="none"
    if possible=="true":
        res+=count
print(res)
