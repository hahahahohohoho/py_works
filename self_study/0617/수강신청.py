import sys

N, M = map(int, input().split())
dic = {}
for i in range(M):
    dic[sys.stdin.readline().rstrip()] = i

res = sorted(dic.items(), key = lambda x:x[1])
if(N > len(res)):
    N = len(res)
    
for i in range(N):
    print(res[i][0])