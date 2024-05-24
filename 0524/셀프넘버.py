def selNum(num) :
    x=list(str(num))
    sum = 0
    for i in range(len(x)):
        sum += int(x[i])
    sum = sum + num
    return sum

arr= set()
for i in range(10000):
    arr.add(selNum(i))
for i in range(1, 10001):
    if i not in arr :
        print(i)