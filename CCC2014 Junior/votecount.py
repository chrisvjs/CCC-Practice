v = int(input())
vchar = input()

aVotes = vchar.count('A')
bVotes = vchar.count('B')


if aVotes > bVotes:
    print('A')
elif bVotes > aVotes:
    print('B')
elif bVotes == aVotes:
    print('Tie')