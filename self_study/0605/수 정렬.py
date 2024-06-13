import sys
arr = []
N = int(sys.stdin.readline())
for _ in range(N):
    arr.append(sys.stdin.readline())
arr = sorted(arr)
for i in arr : 
    print(i)