file1 = open('input.txt', 'r')
Patterns = file1.read().split("\n\n")
Patterns = [p.split('\n') for p in Patterns]

# Validate if a double line is really a reflection until one border
# inputs are the pattern to be checked and then line BEFORE the reflection
def validate(pat, line):
    fixed=False
    if line < len(pat)-(line+2):
        # go to start
        for j in range(line+1):
            if pat[line-j] != pat[line+1+j]:
                print('no proper reflection')
                if fixed:
                    return False
                else:
                    fixed=fix_it(pat[line-j], pat[line+1+j])
                if not fixed:
                    return False
    else:
        # go to end
        for j in range(len(pat)-(line+2)+1):
            if pat[line-j] != pat[line+1+j]:
                print('no proper reflection')
                if fixed:
                    return False
                else:
                    fixed=fix_it(pat[line-j], pat[line+1+j])
                if not fixed:
                    return False
    print(fixed)
    if fixed:
        return True
    else:
        return False

def fix_it(line1, line2):
    print('try to fix it')
    changed=False
    for k,c in enumerate(line1):
        print(k)
        if c != line2[k]:
            if changed:
                return False
            else:
                changed=True
    return True

# search reflection lines
res=0
for pattern in Patterns:
    skip_vert=False
    for i in range(len(pattern)-1):
        if pattern[i] == pattern[i+1] or abs(pattern[i].count('#')-pattern[i+1].count('#')) == 1 :
            if validate(pattern, i):
                #add to res
                res+=100*(i+1)
                skip_vert=True
                break
    if not skip_vert:
        s=''
        transpose=list(map(s.join, zip(*pattern)))
        for i in range(len(transpose)-1):
            print(abs(transpose[i].count('#')-transpose[i+1].count('#')))
            if transpose[i] == transpose[i+1] or abs(transpose[i].count('#')-transpose[i+1].count('#')) == 1 :
                if validate(transpose, i):
                    #add to res
                    res+=i+1
                    break

print(res)
