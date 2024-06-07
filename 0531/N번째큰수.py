N = int(input())
res = []
for i in range(N):
    arr=sorted(map(int, input().split()), reverse= True)
    res.append(arr[2])
for i in res:
    print(i)