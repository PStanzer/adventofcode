file = open('input.txt', 'r')

lines = file.read().split("\n")
lines.pop()
stones=lines[0].split()
print(stones)

def apply(stone):
    #print(stone)
    if stone == "0":
        return ["1"]
    elif len(stone)%2 == 0:
        #print("EVEN")
        #print(stone[:int(len(stone)/2)])
        #print(stone[int(len(stone)/2):])
        return [str(int(stone[:int(len(stone)/2)])), str(int(stone[int(len(stone)/2):]))]
    else:
        return [str(int(stone)*2024)]

for i in range(25):
    print(i)
    new_stones=[]
    for stone in stones:
        for res in apply(stone):
            new_stones.append(res)
    stones=new_stones
    #print(stones)

print(len(stones))
