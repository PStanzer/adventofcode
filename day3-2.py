file1 = open('input.txt', 'r')
Lines = file1.readlines()
len=len(Lines[0])

def check_gear(lineno, pos):
	cnt=0
	mul=1
	#check before
	if pos != 0:
		i=1
		num=''
		while Lines[lineno][pos-i].isdigit():
			num=Lines[lineno][pos-i]+num
			i+=1
		if num != '':
			mul=mul*int(num)
			cnt+=1
	#check after
	if pos != len-1:
		i=1
		num=''
		while Lines[lineno][pos+i].isdigit():
			num=num+Lines[lineno][pos+i]
			i+=1
		if num != '':
			mul=mul*int(num)
			cnt+=1
	if cnt == 2:
		return mul
	#check above
	if lineno != 0:
			if Lines[lineno-1][pos].isdigit():
				i=0
				num=''
				while Lines[lineno-1][pos+i].isdigit():
					num=num+Lines[lineno-1][pos+i]
					i+=1
				i=1
				while Lines[lineno-1][pos-i].isdigit():
					num=Lines[lineno-1][pos-i]+num
					i+=1
				if num != '':
					mul=mul*int(num)
					cnt+=1
				if cnt == 2:
					return mul
			else:
				i=1
				num=''
				while Lines[lineno-1][pos+i].isdigit():
					num=num+Lines[lineno-1][pos+i]
					i+=1
				if num != '':
					mul=mul*int(num)
					cnt+=1
				if cnt == 2:
					return mul
				i=1
				num=''
				while Lines[lineno-1][pos-i].isdigit():
					num=Lines[lineno-1][pos-i]+num
					i+=1
				if num != '':
					mul=mul*int(num)
					cnt+=1
				if cnt == 2:
					return mul
	#check below
	if lineno != 139:
			if Lines[lineno+1][pos].isdigit():
				i=0
				num=''
				while Lines[lineno+1][pos+i].isdigit():
					num=num+Lines[lineno+1][pos+i]
					i+=1
				i=1
				while Lines[lineno+1][pos-i].isdigit():
					num=Lines[lineno+1][pos-i]+num
					i+=1
				if num != '':
					mul=mul*int(num)
					cnt+=1
				if cnt == 2:
					return mul
			else:
				i=1
				num=''
				while Lines[lineno+1][pos+i].isdigit():
					num=num+Lines[lineno+1][pos+i]
					i+=1
				if num != '':
					mul=mul*int(num)
					cnt+=1
				if cnt == 2:
					return mul
				i=1
				num=''
				while Lines[lineno+1][pos-i].isdigit():
					num=Lines[lineno+1][pos-i]+num
					i+=1
				if num != '':
					mul=mul*int(num)
					cnt+=1
				if cnt == 2:
					return mul
	return 0

count=0
res=0
for line in Lines:
    for i, c1 in enumerate(line):
        if c1 == '*':
        	res+=check_gear(count, i)
    count += 1
print(res)
