from collections import defaultdict

f = open('sample.txt', 'r')
info = f.read()
strArry = info.splitlines()
n = len(strArry)
total = 0
N = defaultdict(int)
for i, s in enumerate(strArry):
    winning_cards = []
    N[i] += 1
    temp = 0
    my_cards = []
    val = 0
    card = s.split()
    for j in card:
        if(j == '|'):
            temp = 1
            continue
        if(j.isnumeric() and temp == 0):
            winning_cards.append(int(j))
        if(j.isnumeric() and temp == 1):
            my_cards.append(int(j))
    for k in winning_cards:
        if k in my_cards:
            val += 1
    for j in range(val):
        N[i + 1 + j] += N[i]
print(sum(N.values()))
