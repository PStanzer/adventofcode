from collections import defaultdict
import copy, math

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
mp = 0
qt = 0
qb = 0
ng = 0
for i in range(1000000000):
    queue=[('button','low','broadcaster')]
    for q in queue:
        send(q)
    if ('ng', 'high', 'dr') in queue:
        ng=i+1
    if ('qb', 'high', 'dr') in queue:
        qb=i+1
    if ('qt', 'high', 'dr') in queue:
        qt=i+1
    if ('mp', 'high', 'dr') in queue:
        mp=i+1
    if mp != 0 and qt != 0 and qb != 0 and ng != 0:
        break
    if modules == cache:
        print(i+1, 'REPEAT')
        break

print(math.lcm(mp, qt, qb, ng))
