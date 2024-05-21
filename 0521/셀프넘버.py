def selNum(num) :
    n1 = len(str(num))
    num=int(num)
    arr= [num%10]
    sum = 0
    for i in range(1, n1):
        arr.append(num // 10**i)
    for i in arr :
        sum += i
    return num + sum
