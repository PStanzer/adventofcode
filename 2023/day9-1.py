file1 = open('input.txt', 'r')
Lines = file1.read().split("\n")

def get_stepsize(dataset):
    return [dataset[i+1]-dataset[i] for i in range(len(dataset)-1)]

def get_lasts(inp):
    lasts = [inp[-1]]
    while not all(num == 0 for num in get_stepsize(inp)):
        inp=get_stepsize(inp)
        lasts.append(inp[-1])
    return lasts

def predict_next(line):
    return sum(get_lasts(line))

res=0
for line in Lines:
    res+=predict_next(list(map(int,line.split())))
    
print(res)
