f = open('sample.txt', 'r')
info = f.read()
strArry = info.splitlines()
n = len(strArry)
seeds = [int(i) for i in strArry[0].split() if i.isnumeric()]
soil = []
fertilizer = []
water = []
light = []
temp = []
humidity = []
location = []
ans = [0]*len(seeds)
for ind,i in enumerate(strArry):
    if i.startswith("seed-to-soil map"):
        j = ind + 1
        while(strArry[j]!=""):
            soil.append(strArry[j])
            j+=1
    if i.startswith("soil-to-fertilizer"):
        j = ind + 1
        while (strArry[j] != ""):
            fertilizer.append(strArry[j])
            j += 1
    if i.startswith("fertilizer-to-water"):
        j = ind + 1
        while (strArry[j] != ""):
            water.append(strArry[j])
            j += 1
    if i.startswith("water-to-light"):
        j = ind + 1
        while (strArry[j] != ""):
            light.append(strArry[j])
            j += 1
    if i.startswith("light-to-temperature"):
        j = ind + 1
        while (strArry[j] != ""):
            temp.append(strArry[j])
            j += 1
    if i.startswith("temperature-to-humidity"):
        j = ind + 1
        while (strArry[j] != ""):
            humidity.append(strArry[j])
            j += 1
    if i.startswith("humidity-to-location"):
        j = ind + 1
        while (j<len(strArry)):
            location.append(strArry[j])
            j += 1

for ind,i in enumerate(seeds):
    for inx,j in enumerate(soil):
        mp = j.split()
        if(i>= int(mp[1]) and i <= (int(mp[1])+int(mp[2])-1)):
            ans[ind] = (int(mp[0]) + (i - int(mp[1])))
    if(ans[ind]==0):
        ans[ind] = i

for ind,i in enumerate(ans):
    for inx,j in enumerate(fertilizer):
        mp = j.split()
        if(i>= int(mp[1]) and i <= (int(mp[1])+int(mp[2])-1)):
            ans[ind] = (int(mp[0]) + (i - int(mp[1])))

for ind, i in enumerate(ans):
    for inx, j in enumerate(water):
        mp = j.split()
        if (i >= int(mp[1]) and i <= (int(mp[1]) + int(mp[2]) - 1)):
            ans[ind] = (int(mp[0]) + (i - int(mp[1])))

for ind, i in enumerate(ans):
    for inx, j in enumerate(light):
        mp = j.split()
        if (i >= int(mp[1]) and i <= (int(mp[1]) + int(mp[2]) - 1)):
            ans[ind] = (int(mp[0]) + (i - int(mp[1])))

for ind, i in enumerate(ans):
    for inx, j in enumerate(temp):
        mp = j.split()
        if (i >= int(mp[1]) and i <= (int(mp[1]) + int(mp[2]) - 1)):
            ans[ind] = (int(mp[0]) + (i - int(mp[1])))

for ind, i in enumerate(ans):
    for inx, j in enumerate(humidity):
        mp = j.split()
        if (i >= int(mp[1]) and i <= (int(mp[1]) + int(mp[2]) - 1)):
            ans[ind] = (int(mp[0]) + (i - int(mp[1])))

for ind, i in enumerate(ans):
    for inx, j in enumerate(location):
        mp = j.split()
        if (i >= int(mp[1]) and i <= (int(mp[1]) + int(mp[2]) - 1)):
            ans[ind] = (int(mp[0]) + (i - int(mp[1])))

print(min(ans))


