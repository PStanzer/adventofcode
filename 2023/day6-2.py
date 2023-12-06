file1 = open('input.txt', 'r')
Lines = file1.readlines()

times=int(Lines[0].split(':')[1].replace(' ',''))
records=int(Lines[1].split(':')[1].replace(' ',''))

def ways_to_win(time,record):
    for i in range(time):
        if i*(time-i) > record:
            return time-(2*i-1)
        i+=1

print(ways_to_win(times,records))
