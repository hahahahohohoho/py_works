a = int(input())

for i in range(a):
    inp1, inp2 = input().split()
    inp1 = int(inp1)
    k = str(inp2)
    for j in k:
        print(j*inp1, end='')
