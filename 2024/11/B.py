file = open('input.txt', 'r')

lines = file.read().split("\n")
lines.pop()
stones=[int(stone) for stone in lines[0].split()]
print(stones)

lookup={0:[1]}

def apply(stone):
    #print(stone)
    if stone in lookup:
        return lookup[stone]
    if len(str(stone))%2 == 0:
        lookup[stone] = [int(str(stone)[:int(len(str(stone))/2)]), int(str(stone)[int(len(str(stone))/2):])]
    else:
        lookup[stone] =  [stone*2024]
    return lookup[stone]

current={}
for stone in stones:
    if stone not in current:
        current[stone] = 1
    else:
        current[stone] = current[stone]+1

for i in range(75):
    #print(i, stone)
    tmp_stones={}
    for j,st in enumerate(current):
        #print(st,current[st])
        for res in apply(st):
            if res not in tmp_stones:
                tmp_stones[res] = 1*current[st]
            else:
                tmp_stones[res] += 1*current[st]
    current=tmp_stones
    #print(current)

print(sum(current.values()))


exit()


for stone in stones:
    new_stones=[stone]
    for i in range(6):
        #print(i, stone)
        tmp_stones=[]
        for st in new_stones:
            for res in apply(st):
                tmp_stones.append(res)
        new_stones=tmp_stones
        #print(new_stones)
        print(i, len(new_stones))
    sum+=len(new_stones)

#print(all_stones)
print(sum)
