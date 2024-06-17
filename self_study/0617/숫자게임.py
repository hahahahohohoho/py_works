import itertools
N = int(input())
arr = [0] * N
for i in range(N):
    inp = list(map(int, input().split()))
    ncr = list(itertools.combinations(inp, 3))
    max_res = 0
    for j in range(len(ncr)) :
        if sum(ncr[j]) %10 > max_res :
            max_res = sum(ncr[j])%10
    arr[i] = max_res

# 가장 높은 숫자 출력
for i in range(N-1, -1, -1):
    if max(arr) == arr[i] :
        print(i+1)
        break

