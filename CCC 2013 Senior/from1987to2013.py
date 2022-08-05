n = int(input())

def unique(n):
    s = str(n)
    for i in s:
        if s.count(i) >1:
            return False
    return True

while not unique(n+1):
    n+=1
print(n+1)