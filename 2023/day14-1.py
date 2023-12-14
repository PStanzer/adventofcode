file1 = open('input.txt', 'r')
Lines = file1.read().split("\n")

RRP=[] #list of round rock positions
leng=len(Lines)
for j in range(len(Lines[0])):
	stopper=-1
	cnt=1
	for i,line in enumerate(Lines):
		if line[j] == '#':
			stopper=i
			cnt=1
		elif line[j] == 'O':
			RRP.append(leng-stopper-cnt)
			cnt+=1
		
print(sum(RRP))
