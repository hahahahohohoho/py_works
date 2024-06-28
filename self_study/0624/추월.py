import sys

N = int(sys.stdin.readline())
firstCar = {}
out = []
cnt = 0
for i in range(N) :
    firstCar[str(sys.stdin.readline().rstrip("\n"))] = i
for i in range(N) :
    out.append(str(sys.stdin.readline().rstrip("\n")))
for j in range(N - 1):
    for k in range(j + 1, N):
        if firstCar[out[j]] > firstCar[out[k]]:
            cnt += 1
            break
print(cnt)