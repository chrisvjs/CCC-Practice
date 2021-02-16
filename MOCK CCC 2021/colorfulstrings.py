from itertools import permutations
rstr = input()

perms = [''.join(p) for p in permutations(rstr)]
r = list(dict.fromkeys(perms))

def uniqueCharacters(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)): 
            if(str[i] == str[j]):
                return False
    return True

cS = []
for i in r:
    if uniqueCharacters(i):
        cS.append(i)

p = len(cS)

print(p)