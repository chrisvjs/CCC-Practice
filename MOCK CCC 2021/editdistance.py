eS = input()
S = input()

def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele   
    return str1  

alpha = list(eS)
ori = list(S)

words = []

for i in alpha:
    for s in range(len(ori)):
        o = list(S)
        t = list(S)
        l = list(S)
        o[s] += i
        del t[s]
        l[s] == i
        words.append(listToString(o))
        words.append(listToString(t))
        words.append(listToString(l))


r = list(dict.fromkeys(words))
sorted(r)
print(r)

