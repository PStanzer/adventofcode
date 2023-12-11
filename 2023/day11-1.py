file1 = open('input.txt', 'r')
Lines = file1.read().split("\n")

galaxies=[]
i=0
for line in Lines:
	if not line.find('#') == -1:
		for j, x in enumerate(line):
			if x == '#':
				galaxies.append([i,j])
	else:
		i+=1
	i+=1

exp=-1
for j in range(len(Lines[0])):
	empty=True
	for n in range(len(Lines)):
		if Lines[n][j] == '#':
			empty=False
			break
	if empty:
		exp+=1
		for gal in galaxies:
			if gal[1] > j+exp:
				gal[1]+=1

res=0
for k, gal in enumerate(galaxies):
	for m in range(k+1,len(galaxies)):
		res+=abs(gal[0]-galaxies[m][0])+abs(gal[1]-galaxies[m][1])

print(res)