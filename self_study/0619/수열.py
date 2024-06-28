import sys
T, step = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
dic = {}
for i in range(0, T-step+1):
    dic[i] = sum(arr[i:i+step])
print(max(dic.values()))

# 시간초과로 풀지 못함.....