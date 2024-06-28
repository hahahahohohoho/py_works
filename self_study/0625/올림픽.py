import sys
from functools import cmp_to_key
input = sys.stdin.readline
N, K = map(int, input().split())
medals = []
for _ in range(N):
    medals.append(list(map(int, input().split())))
# 람다 식을 통한 정렬 방식 구현
medals.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)
idx = [medals[i][0] for i in range(N)].index(K)

for i in range(N):
    if medals[idx][1:] == medals[i][1:]:
        print(i+1)
        break

