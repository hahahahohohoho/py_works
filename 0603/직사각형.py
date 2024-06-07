lst = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            lst[i][j]=1
sum = 0
for i in range(len(lst)) :
    for j in range(len(lst[0])):
        sum += lst[i][j]
print(sum)
