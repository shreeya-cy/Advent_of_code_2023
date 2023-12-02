f = open('sample.txt', 'r')
info = f.read()
strArry = info.splitlines()
n = len(strArry)
totalSum = 0
for i in range(0,n):
    game = strArry[i].split()
    j = 2
    r = list()
    b = list()
    g = list()
    power = 0
    while (j < len(game) - 1):
        if game[j + 1].startswith("blue"):
            b.append(int(game[j]))
        if game[j + 1].startswith("green"):
            g.append(int(game[j]))
        if game[j + 1].startswith("red"):
            r.append(int(game[j]))
        j = j + 2
    power = max(r)*max(g)*max(b)
    totalSum += power
print(totalSum)