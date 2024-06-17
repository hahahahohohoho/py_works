import sys
N=int(input())

cnt, dic = 0, {}
for _ in range(N) :
    a = sys.stdin.readline().strip()
    if a == 'ENTER' :
        dic = {}
    elif a not in dic :
        dic[a] = 0
        cnt +=1
print(cnt)