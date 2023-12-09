file1 = open('input.txt', 'r')
Lines = file1.read().split("\n")

def get_stepsize(dataset):
    return [dataset[i+1]-dataset[i] for i in range(len(dataset)-1)]

def get_firsts(inp):
    firsts = [inp[0]]
    while not all(num == 0 for num in get_stepsize(inp)):
        inp=get_stepsize(inp)
        firsts.append(inp[0])
    return firsts

def predict_prev(line):
    firsts=get_firsts(line)
    return sum(firsts[::2])-sum(firsts[1::2])

res=0
for line in Lines:
    res+=predict_prev(list(map(int,line.split())))
    
print(res)
