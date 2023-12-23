from collections import defaultdict
import copy

file1 = open('input.txt', 'r')
Lines = file1.read().split("\n")

modules=defaultdict()
for line in Lines:
    if line.split()[0] == 'broadcaster':
        modules['broadcaster']={'kind':'broadcaster', 'dest':tuple(line.split(' -> ')[1].split(', '))}
    elif line[0] == '%':
        modules[line.split(' -> ')[0][1:]]={'kind':line[0], 'status':'off', 'dest':tuple(line.split(' -> ')[1].split(', '))}
    else:
        modules[line.split(' -> ')[0][1:]]={'kind':line[0], 'status':defaultdict(), 'dest':tuple(line.split(' -> ')[1].split(', '))}

for mod in modules:
    if modules[mod]['kind'] == '&':
        for x,y in modules.items():
            if mod in y['dest']:
                modules[mod]['status'][x]='low'

def send(item):
    sender,pulse,target=item
    if target == 'rx':
        return
    if target == 'broadcaster':
        for d in modules['broadcaster']['dest']:
            queue.append((target,pulse,d))
    else:
        if modules[target]['kind'] == '%':
            if pulse == 'low':
                if modules[target]['status'] == 'off':
                    modules[target]['status'] = 'on'
                    pulse='high'
                else:
                    modules[target]['status'] = 'off'
                for d in modules[target]['dest']:
                    queue.append((target,pulse,d))
        elif modules[target]['kind'] == '&':
            modules[target]['status'][sender]=pulse
            if 'low' in modules[target]['status'].values():
                pulse='high'
                for d in modules[target]['dest']:
                    queue.append((target,pulse,d))
            else:
                pulse='low'
                for d in modules[target]['dest']:
                    queue.append((target,pulse,d))
            
cache=copy.deepcopy(modules)
lo=0
hi=0
for i in range(1000):
    queue=[('button','low','broadcaster')]
    for q in queue:
        if q[1] == 'low':
            lo+=1
        else:
            hi += 1
        send(q)
    if modules == cache:
        print(i+1, 'REPEAT')
        break

print('lo:',lo,'hi:',hi,'multi:',lo*hi)
