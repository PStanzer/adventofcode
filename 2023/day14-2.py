file1 = open('input.txt', 'r')
Lines = file1.read().replace('\n',' ')

def rotate90_clockwise(p):
    return ' '.join(map(''.join,zip(*(p.split())[::-1])))

def roll(grid):
    while 'O.' in grid:
        grid=grid.replace('O.','.O')
    return grid

def calc_load(grid):
    res=0
    for r in grid.split():
        for i,c in enumerate(r):
            if c == 'O':
                res+=i+1
    return res

#start with map rotated so that north is to the right
grid=Lines
cache=[]
res_it=10000000000
for n in range(500):
    #north
    grid=roll(rotate90_clockwise(grid))
    #west
    grid=roll(rotate90_clockwise(grid))
    #south
    grid=roll(rotate90_clockwise(grid))
    #east
    grid=roll(rotate90_clockwise(grid))
    #calc
    load=calc_load(rotate90_clockwise(grid))
    if grid in cache:
        print(n, n-cache.index(grid))
        res_it=n+(999999999-n)%(n-cache.index(grid))
    cache.append(grid)
    if n == res_it:
        print(n,load)
        break
