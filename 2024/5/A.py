file = open('input.txt', 'r')
input=file.read().split("\n")
rules = [rule.split("|") for rule in input if "|" in rule]
updates = [up for up in input if "," in up]

print(rules)
print(updates)

def check_rules(u_split,page,pos):
    for rule in rules:
        #print(rule)
        if page == int(rule[0]):
            #print(page,"before",rule[1],"? at",pos)
            if int(rule[1]) not in u_split:
                continue
            else:
                #print(u_split.index(int(rule[1])))
                if pos < u_split.index(int(rule[1])):
                    #print("OK")
                    continue
                else:
                    print("failed at",rule)
                    return False
        elif page == int(rule[1]):
            #print(page,"after",rule[0],"? at",pos)
            if int(rule[0]) not in u_split:
                continue
            else:
                #print(u_split.index(int(rule[1])))
                if pos > u_split.index(int(rule[0])):
                    continue
                else:
                    print("failed at",rule)
                    return False
        else:
            #print(page,"NOT FOuND")
            continue
    return True

res=0
for update in updates:
    u_split=[int(us) for us in update.split(",")]
    print(u_split)
    good=True
    for i,page in enumerate(u_split):
        if not check_rules(u_split,page,i):
            print("wrong update at",u_split,page,i)
            good=False
            break
    if good:
        print("good update",update,len(u_split))
        res+=u_split[(len(u_split)-1)//2]

print(res)

