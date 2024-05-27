N = input()
while '9' in N :
    N = N.replace('9', '6')
N = map(int, N)
arr = [1,2,3,4,5,6,7,8,6]
result = 1
for i in N :
    if i in arr :
        arr.remove(i)
    else :
        arr = [1,2,3,4,5,6,7,8,6]
        arr.remove(i)
        result +=1
print(result)