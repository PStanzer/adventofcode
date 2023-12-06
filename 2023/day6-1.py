file1 = open('input.txt', 'r')
Lines = file1.readlines()

times=[int(x) for x in Lines[0].split(':')[1].split()]
records=[int(x) for x in Lines[1].split(':')[1].split()]

def ways_to_win(time,record):
    for i in range(time):
        if i*(time-i) > record:
            return time-(2*i-1)
        i+=1

res=1
for k in range(len(times)):
    res *= ways_to_win(times[k],records[k])
print(res)
