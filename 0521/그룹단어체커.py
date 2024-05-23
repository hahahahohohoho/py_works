N = int(input())

result = 0
for _ in range(N):
    A = input()
    sum = 0
    d =[A[0]]
    for i in range(1, len(A)):
        if A[i-1] != A[i] :
            d.append(A[i])
    for i in range(len(d)) :
        if d.count(d[i]) == 1 :
            sum += 1
    if sum == len(d):
        result +=1
print(result)