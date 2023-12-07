from collections import Counter

file1 = open('input.txt', 'r')
lines = file1.read().split("\n")

hands = [line.split()[0] for line in lines]
bids= [int(line.split()[1]) for line in lines]
list_of_tuples = list(zip(hands,bids))
value={'A':14,'K':13,'Q':12,'J':1,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}

def commons(hand):
    order=Counter(hand).most_common(2)
    if order[0][1] == 5:
        return (5,0)
    elif order[0][0] == 'J':
        return (int(order[1][1]+hand.count('J')),1)
    elif order[1][0] == 'J':
        return (int(order[0][1]+hand.count('J')),1)
    else:
        return (order[0][1]+hand.count('J'),order[1][1])

list_of_tuples.sort(key = lambda x: (int(value[x[0][0]]),int(value[x[0][1]]),int(value[x[0][2]]),int(value[x[0][3]]),int(value[x[0][4]])))
list_of_tuples.sort(key = lambda x: commons(x[0]))

res=0
i=1
for bid in list_of_tuples:
    res+=i*bid[1]
    i+=1

print(res)
