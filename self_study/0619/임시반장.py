N = int(input())
arr = []
res = [0]*N
for i in range(N):
    arr.append(list(map(int, input().split())))
    res[i] = [0] * N
for i in range(5):
    for j in range(N):
        for k in range(j+1, N):
            if arr[j][i] == arr[k][i] :
                res[k][j] = 1
                res[j][k] = 1
for i in range(N) :
    res[i] = sum(res[i])
print(res.index(max(res))+1)
