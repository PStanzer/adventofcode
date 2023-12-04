file1 = open('input.txt', 'r')
Lines = file1.readlines()

count=0
res=0
for line in Lines:
    match=-1
    card=line.strip().split(':')[1].split('|')
    for n in card[0].split():
    	if card[1].split().count(n) == 1:
    		match +=1
    	elif card[1].split().count(n) == 2:
    		print('WARN DOUBLE MATCH')
    print(card)
    if match != -1:
    	res += pow(2,match)
    count += 1
print(res)
