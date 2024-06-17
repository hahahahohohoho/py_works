import sys
N = int(input())
arr = []
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    arr.append(a)

print(arr)
# for i  in range(N):
#     for j  in range(1, 6) :
        