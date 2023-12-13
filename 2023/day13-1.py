file1 = open('input.txt', 'r')
Patterns = file1.read().split("\n\n")
Patterns = [p.split('\n') for p in Patterns]

# Validate if a double line is really a reflection until one border
# inputs are the pattern to be checked and then line BEFORE the reflection
def validate(pat, line):
    if line < len(pat)-(line+2):
        # go to start
        for j in range(1,line+1):
            if pat[line-j] != pat[line+1+j]:
                print('no proper reflection')
                return False
    else:
        # go to end
        for j in range(1,len(pat)-(line+2)+1):
            if pat[line-j] != pat[line+1+j]:
                print('no proper reflection')
                return False
    return True

# search reflection lines
res=0
for pattern in Patterns:
    skip_vert=False
    for i in range(len(pattern)-1):
        if pattern[i] == pattern[i+1]:
            if validate(pattern, i):
                #add to res
                res+=100*(i+1)
                skip_vert=True
                break
    if not skip_vert:
        s=''
        transpose=list(map(s.join, zip(*pattern)))
        for i in range(len(transpose)-1):
            if transpose[i] == transpose[i+1]:
                if validate(transpose, i):
                    #add to res
                    res+=i+1
                    break

print(res)
