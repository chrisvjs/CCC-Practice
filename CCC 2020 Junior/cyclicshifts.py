text = input()
string = input()
a = 'no'

for i in range(len(string)):
    if string in text:
        a = 'yes'
        break
    string = string[-1] + string[:-1]

print(a)
