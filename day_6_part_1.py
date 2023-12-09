import numpy as np

f = open('sample.txt', 'r')
info = f.read()
strArry = info.splitlines()
time = []
distance = []
for i in strArry:
    if i.startswith("Time"):
        temp_arr = i.split()
        for j in temp_arr:
            if j.isnumeric():
                time.append(int(j))
    if i.startswith("Distance"):
        temp_arr = i.split()
        for j in temp_arr:
            if j.isnumeric():
                distance.append(int(j))
counts = []
for ind,i in enumerate(time):
    count = 0
    for j in range(1,i):
        if ((i-j) * j) > distance[ind]:
            count += 1
    counts.append(count)
product = np.prod(counts)
print(product)
