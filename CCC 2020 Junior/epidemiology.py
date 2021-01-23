p = int(input())
n =  int(input())
r = int(input())

infected = n
people = n
count = 0

while True:
    people = people + (infected * r)
    infected = infected  * r
    count += 1
    if people >= p:
        if people == p:
            print (count+1)
        else:
            print (count)
        break


    