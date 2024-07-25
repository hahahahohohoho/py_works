import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for _ in range(N) :
    a = input().rstrip()
    if len(a) < M :
        continue
    else :
        if a in dic :
            dic[a] += 1
        else :
            dic[a] = 1
            
result = sorted(dic.items(), key= lambda x : (-x[1], -len(x[0]), x[0]))
for i in result:
    print(i[0])