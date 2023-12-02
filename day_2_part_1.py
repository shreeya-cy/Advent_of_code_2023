f = open('sample.txt', 'r')
info = f.read()
strArry = info.splitlines()
n = len(strArry)
totalSum = (n*(n+1))/2
for i in range(0,n):
    game = strArry[i].split()
    j = 2
    r = 0
    b = 0
    g = 0
    while(j<len(game)-1):
        if game[j+1].startswith("blue"):
            b = game[j]
            if int(b) > 14:
                totalSum -= (i+1)
                break
            if game[j+1].endswith(";"):
                r = 0
                b = 0
                g = 0
        if game[j+1].startswith("green"):
            g = game[j]
            if int(g) > 13:
                totalSum -= (i+1)
                break
            if game[j+1].endswith(";"):
                r = 0
                b = 0
                g = 0
        if game[j+1].startswith("red"):
            r = game[j]
            if int(r) > 12:
                totalSum -= (i+1)
                break
            if game[j+1].endswith(";"):
                r = 0
                b = 0
                g = 0
        j = j+2
print(totalSum)



