import itertools

file = open('input.txt', 'r')

lines = file.read().split("\n")
lines.pop()

res=0

def check_perm(res,nums,perm):
    calc=int(nums[0])
    for i,op in enumerate(perm):
        match op:
            case "+":
                #print(calc,"+",nums[i+1])
                calc+=int(nums[i+1])
            case "*":
                #print(calc,"*",nums[i+1])
                calc*=int(nums[i+1])
        if calc > int(res):
            #print("too big")
            return False
    if calc == int(res):
        #print("TRUE")
        return True
    else:
        return False
    
def check_line(result,numbers):
    for perm in list(itertools.product(["+","*"], repeat=len(numbers)-1)):
        #print(result,numbers)
        #print(perm)
        if check_perm(result,numbers,perm):
            #print(line,perm)
            return True
    return False

for line in lines:
    split_lines=line.split(": ")
    nums=split_lines[1].split(" ")
    if check_line(split_lines[0],nums):
        res+=int(split_lines[0])

print(res)
