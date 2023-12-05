file1 = open('input.txt', 'r')
Lines = file1.readlines()

seeds=Lines[0].strip().split(':')[1].strip().split()
count=-1
maps=[]

for line in Lines:
     if line == '\n' or line.find('seeds') != -1:
         continue
     elif -1 != line.find('-'):
         maps.append([])
         count+=1
     else:
         maps[count].append(line.split())

#print(seeds)

def find_in_map(in_val,search_map):
     for i in range(len(search_map)):
         if int(in_val) >= int(search_map[i][0]) and int(in_val) < int(search_map[i][0])+int(search_map[i][2]):
             return int(in_val)-int(search_map[i][0])+int(search_map[i][1])
     return in_val

def check_seed(seed):
    for j in range(0,int(len(seeds)),2):
        #print(seeds[j],seeds[j+1])
        if seed >= int(seeds[j]) and seed < int(seeds[j])+int(seeds[j+1]):
            return True

n=1
while True:
    inp=n
    if n % 10000 == 0:
        print(inp)
    for k in range(len(maps)-1,-1,-1):
        inp=find_in_map(inp,maps[k])
    #print('Out',inp)
    if check_seed(inp):
        print('ok:',n)
        break
    n+=1


