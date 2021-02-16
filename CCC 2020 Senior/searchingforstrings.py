from itertools import permutations

n = input()
lenN = len(n)
h = input()
lenH = len(h)

split = []
perms = [''.join(p) for p in permutations(n)]
perms = list(dict.fromkeys(perms))
count = 0

for index in range(0, lenH, 1):
    split.append(h[index : index + lenN])

split = list(dict.fromkeys(split))

for q in perms:
    if q in split:
        count +=1

print(count)