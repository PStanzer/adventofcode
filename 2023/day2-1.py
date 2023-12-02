file1 = open('input.txt', 'r')
Lines = file1.readlines()
count=0
res=0
for line in Lines:
    possible="true"
    count += 1
    color="none"
    print("{}".format(line.strip()))
    for w in line.split():
        #print(w)
        if color != "none":
            print( w.strip(',;')," ",color)
            print(color.find(w.strip(',;')))
            if 0 == color.find(w.strip(',;')):
                print("OK")
                color="none"
            else:
                print("color vio")
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
print(res)
                
