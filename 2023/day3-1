file1 = open('input.txt', 'r')
Lines = file1.readlines()
len=len(Lines[0])

def check_symbol(lineno, start, end):
	if start==0:
		start=1
	if end==len-2:
		end=len-3
	if Lines[lineno][start-1] != '.' and not Lines[lineno][start-1].isdigit():
		return True
	elif Lines[lineno][end+1] != '.' and not Lines[lineno][end+1].isdigit():
		return True
	for c in Lines[lineno-1][start-1:end+2]:
		if c != '.' and not c.isdigit():
			return True
	if not lineno==139:
		for c in Lines[lineno+1][start-1:end+2]:
			if c != '.' and not c.isdigit():
				return True

count=0
res=0
for line in Lines:
    number=False
    start=0
    end=0
    for i, c1 in enumerate(line):
        if c1.isdigit() and not number:
        	number=True
        	start=i
        	end=i
        elif c1.isdigit() and number:
        	end=i
        elif not c1.isdigit() and number:
        	#call function to check
        	if check_symbol(count, start, end):
        		partnum=int(line[start:end+1])
        		res+=int(partnum)
        	number=False
    count += 1
print(res)
