import math
from collections import Counter

file1 = open('input.txt', 'r')
Lines = file1.read().split("\n")

symbols = []

numbers = []
for line in Lines:
    symbols.append(list(filter(None,list(line.split()[0].split('.')))))
    numbers.append([int(num) for num in line.split()[1].split(',')])

def rem_obv(sym,num):
    if len(num) == len(sym):
        i=0
        while i < len(sym):
            if num[i] == len(sym[i]):
                num.pop(i)
                sym.pop(i)
                i-=1
            i+=1
    return sym, num

def res_obv(sym,num):
    poss=0
    if len(num) == len(sym):
        if len(num) == 0:
            return poss+1
        for i, s in enumerate(sym):
            poss += math.comb(len(s),num[i])
        return poss
    elif len(sym) == 1 and len(sym[0]) == sum(num)+len(num)-1:
        return poss+1
    elif len(sym) == 1 and sym[0] == len(sym[0]) * sym[0][0]:
        #print('all ?',sym, num)
        #print(len(sym[0])-sum(num)+len(num),len(num)*2-1)
        poss = math.comb(len(sym[0])-sum(num)+len(num),len(num)*2-1) - math.comb(len(sym[0])-sum(num)+len(num)-1,len(num)*2-1)
        return poss

def rem_ends(sym,num):
    print(sym)
    if sym[0] == '':
        return sym, num
    while sym[0][0] == '#':
        sym[0] = sym[0][num[0]+1:]
        num.pop(0)
        if sym[0] == '':
            sym.pop(0)
        if num == []:
            print('END')
            break
    if sym == []:
        return sym, num
    while sym[-1][-1] == '#':
        sym[-1] = sym[-1][:-num[-1]]
        num.pop(-1)
        if sym[-1] == '':
            sym.pop(-1)
        if num == []:
            print('END')
            break
    return sym, num

def res_first(sym,num):
    if '#'*num[0] == sym[0][0:num[0]]:
        sym[0] = sym[num[0]+1:]
        num.pop(0)
    elif '#'*num[0] == sym[0][1:num[0]+1]:
        sym[0] = sym[0][num[0]+2:]
        num.pop(0)
    return sym, num

def res_last(sym,num):
    #print('last',num[-1],'cs',sym[-1][-num[-1]:])
    if '#'*num[-1] == sym[-1][-num[-1]:]:
        #print('one')
        sym[-1] = sym[-1][:-num[-1]-1]
        num.pop(-1)
    elif '#'*num[-1] == sym[-1][-num[-1]-1:-1]:
        #print('two')
        sym[-1] = sym[0][:-num[-1]-2]
        num.pop(-1)
    return sym, num
        

print(symbols)
print(numbers)

print('rem_obv')
for i in range(len(symbols)):
    #print('sym',list(filter(None,symbols[i].split('.'))))
    #print('num',numbers[i])
    symbols[i], numbers[i] = rem_obv(symbols[i],numbers[i])

print(symbols)
print(numbers)

res=0
i=0
print('res_obv')
while i < len(symbols):
    res1=res_obv(symbols[i], numbers[i])
    if res1 != None:
        res+=res1
        symbols.pop(i)
        numbers.pop(i)
        i-=1
    i+=1

print(symbols)
print(numbers)

i=0
print('rem_ends')
while i < len(symbols):
    print('sym',symbols[i])
    symbols[i], numbers[i] = rem_ends(symbols[i], numbers[i])
    #print('number',numbers[i])
    if symbols[i] == [] or symbols[i][0] == '' or numbers[i] == []:
        res+=1
        symbols.pop(i)
        numbers.pop(i)
        i-=1
    i+=1

print(symbols)
print(numbers)

i=0
print('res_first')
while i < len(symbols):
    #print('what1',numbers[i],i)
    symbols[i], numbers[i] = res_first(symbols[i], numbers[i])
    #print('what2',numbers[i])
    if symbols[i][0] == '' or numbers[i] == []:
        res+=1
        symbols.pop(i)
        numbers.pop(i)
        i-=1
    i+=1

print(symbols)
print(numbers)

i=0
print('res_last')
while i < len(symbols):
    #print('what1',numbers[i],i)
    symbols[i], numbers[i] = res_last(symbols[i], numbers[i])
    #print('what2',numbers[i])
    if symbols[i][-1] == '' or numbers[i] == []:
        res+=1
        symbols.pop(i)
        numbers.pop(i)
        i-=1
    i+=1

print(symbols)
print(numbers)
print(res)
i=0
print('res_obv')
while i < len(symbols):
    res1=res_obv(symbols[i], numbers[i])
    #print(res1)
    if res1 != None:
        res+=res1
        symbols.pop(i)
        numbers.pop(i)
        i-=1
    i+=1

print(symbols)
print(numbers)

i=0
print('rem_ends')
while i < len(symbols):
    print('sym',symbols[i])
    symbols[i], numbers[i] = rem_ends(symbols[i], numbers[i])
    #print('number',numbers[i])
    if symbols[i] == [] or symbols[i][0] == '' or numbers[i] == []:
        res+=1
        symbols.pop(i)
        numbers.pop(i)
        i-=1
    i+=1

print(symbols)
print(numbers)

print(res)
print(len(symbols))
print(math.comb(5,3)-math.comb(4,3)) #math.comb(len(s),num[i])