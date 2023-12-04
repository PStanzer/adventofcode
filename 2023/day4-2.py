file1 = open('input.txt', 'r')
Lines = file1.readlines()

count=0
instances = [1]*len(Lines)

for line in Lines:
    match=0
    card=line.strip().split(':')[1].split('|')
    for n in card[0].split():
        if card[1].split().count(n) == 1:
            match +=1
    print(card)
    for k in range(1,match+1):
        instances[k+count]+=1*instances[count]
    count += 1
print(sum(instances))
