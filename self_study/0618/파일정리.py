import sys
N = int(input())
dic = {}
for _ in range(N):
    a = sys.stdin.readline().replace('\n', '').split('.')
    if a[1] in dic :
        dic[a[1]] +=1
    else :
        dic[a[1]] =1
dic = sorted(dic.items(), key = lambda item: item[0])
for i in dic :
    print(*i)