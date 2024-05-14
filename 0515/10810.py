a, b = map(int, input().split())

lst = [0 for i in range(a)]
for i in range(b) :
    c, d, e = map(int, input().split())
    for k in range(c-1, d):
        lst[k] =e
for j in lst :
    print(j, end=" ")