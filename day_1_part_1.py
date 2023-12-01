f = open('sample.txt', 'r')
info = f.read()
strArry = info.splitlines()
totalSum = 0
for i in strArry:
    n = len(i)
    d1 = None
    d2 = None
    for j in range(0,n):
        if (i[j].isnumeric()):
            d1 = i[j]
            break
    for j in range(n-1,0,-1):
        if (i[j].isnumeric()):
            d2 = i[j]
            break
    if d2 == None:
        d2 = d1
    num = int(d1)*10 + int(d2)
    totalSum += num
print(totalSum)