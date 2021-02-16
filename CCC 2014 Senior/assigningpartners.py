f = int(input())
t1 = input().split()
t2 = input().split()
compare = {}
y = True
for i in range(f):
    p1 = t1[i]
    p2 = t2[i]
    if p1 in compare.keys():
        if compare[p1] != p2:
            y = False
            break
    if p2 in compare.keys():
        if compare[p2] != p1:
            y = False
            break
    if p1 == p2:
        y = False
        break
    if p1 not in compare.keys(): 
        compare[p1] = p2
    if p2 not in compare.keys(): 
        compare[p2] = p1
print("good" if y else "bad")