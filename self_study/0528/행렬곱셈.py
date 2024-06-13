a, b = map(int, input().split())
arr_a, arr_b = [], []
for i in range(a):
    arr_a.append(list(map(int, input().split())))
c, d = map(int, input().split())
for i in range(c):
    arr_b.append(list(map(int, input().split())))

sum=0
result_arr = [[0 for _ in range(a)] for _ in range(d)]
for i in range(a):
    for j in range(d):
        for k in range(b):
            sum+= arr_a[i][k] * arr_b[k][j]
        result_arr[i][j] = sum
        sum = 0

for i in range(len(result_arr)):
    for j in range(len(result_arr[0])):
        print(result_arr[i][j], end=' ')
    print()       