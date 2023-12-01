a = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

file1 = open('./input/day1-1.txt', 'r')
Lines = file1.readlines()

count = 0
sum = 0
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
    # find first number
    first=99999
    lowest=99999
    for num in range(0,9):
        tmp=line.find(a[num])
        if tmp != -1 and tmp < int(lowest):
            first=num+1
            lowest=tmp
    for i, c1 in enumerate(line):
        if c1.isdigit():
            if i < lowest:
                first=c1
                lowest=i
            break
    print("first:", first, "at", lowest)
    
    # find second number
    second=99999
    lowest=99999
    for num in range(0,9):
        enil=line[::-1]
        tmp=enil.find(a[num][::-1])
        if tmp != -1 and tmp < int(lowest):
            second=num+1
            lowest=tmp
    for i, c2 in enumerate(enil):
        if c2.isdigit():
            if i < lowest:
                second=c2
                lowest=i
                print("i", i)
            break
    print("second:", second, "at", lowest)
    sum+=int(str(first)+str(second))
    
print(sum)
