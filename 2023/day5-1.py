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

def find_in_map(in_val,search_map):
     for i in range(len(search_map)):
         if int(in_val) >= int(search_map[i][1]) and int(in_val) < int(search_map[i][1])+int(search_map[i][2]):
             return int(in_val)-int(search_map[i][1])+int(search_map[i][0])
     return in_val

locations=[]
for seed in seeds:
     inp=seed
     for k in range(len(maps)):
         inp=find_in_map(inp,maps[k])
     locations.append(inp)
print(min(locations))
