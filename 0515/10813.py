inp1, inp2 = map(int, input().split())

lst = [0 for i in range(inp1)]
for i in range(inp1):
    lst[i] = i+1

for i in range(inp2) :
    inp3, inp4 = map(int, input().split())
    temp = lst[inp3-1]
    lst[inp3-1] = lst[inp4-1]
    lst[inp4-1] = temp
for j in lst :
    print(j, end=" ")