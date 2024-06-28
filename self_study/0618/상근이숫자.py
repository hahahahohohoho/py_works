import sys
N = int(input())
arr1 = list(map(int, sys.stdin.readline().split()))
M = int(input())
arr2 = list(map(int, sys.stdin.readline().split()))

dic = {}
for i in arr2:
    dic[i] = 0
for i in arr1:
    if i in dic :
        dic[i] +=1

print(*dic.values())