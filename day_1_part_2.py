f = open('sample.txt', 'r')
info = f.read()
strArry = info.splitlines()
totalSum = 0
nums = ["one","two","three","four","five","six","seven","eight","nine","1","2","3","4","5","6","7","8","9"]
actualnums = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
for i in strArry:
    n = len(i)
    digits = list()
    for j in range(0,n):
        for k in range(0,len(nums)):
            if(i[j:].startswith(nums[k])):
                digits.append(actualnums[k])
    number = (digits[0])*10+(digits[-1])
    totalSum += number
print(totalSum)
