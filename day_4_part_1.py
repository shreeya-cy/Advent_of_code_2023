f = open('sample.txt', 'r')
info = f.read()
strArry = info.splitlines()
n = len(strArry)
total = 0
for i, s in enumerate(strArry):
    winning_cards = []
    my_cards = []
    temp = 0
    card = s.split()
    for j in card:
        if(j == '|'):
            temp = 1
            continue
        if(j.isnumeric() and temp == 0):
            winning_cards.append(int(j))
        if(j.isnumeric() and temp == 1):
            my_cards.append(int(j))
    points = 0
    for k in winning_cards:
        if k in my_cards:
            if(points == 0):
                points = 1
            else:
                points = points*2
    total += points
print(total)
