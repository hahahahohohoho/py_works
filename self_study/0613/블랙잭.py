import itertools
N, M = map(int, input().split())
arr = list(map(int, input().split()))
ncr = list(itertools.combinations(arr, 3))
max = 0
for i in ncr :
    if sum(i) > max and M>=sum(i) :
        max = sum(i)
print(max)