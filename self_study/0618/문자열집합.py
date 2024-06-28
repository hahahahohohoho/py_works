import sys
N, M = map(int, input().split())

dic, arr = {}, []
for _ in range(N):
    dic[sys.stdin.readline().rstrip()] = 0
for _ in range(M):
    arr.append(sys.stdin.readline().rstrip())

for i in arr :
    if i in dic :
        dic[i] +=1
print(sum(dic.values()))