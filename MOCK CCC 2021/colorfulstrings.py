r = []

def subs(s, op, i, j):

    if(i == m):
        op[j] = None
        temp = "".join([i for i in op if i] )

        r.append(temp)
        return

    else:
        op[j] = s[i]
 
        subs(s, op, 
                     i + 1, j + 1)
        subs(s, op, 
                     i + 1, j)
        
w = input()
m = len(w)
n = (2 ** m) +1
 
op = [None for i in range(n)]

subs(w, op, 0, 0)
 
print(len(set(r)))