inp1, inp2 = map(int, input().split())

lst = [0 for i in range(inp1)]
for i in range(inp1):
    lst[i] = i+1
for i in range(inp2) :
    inp3, inp4 = map(int, input().split())
    revLst = lst[inp3-1:inp4].reverse()
    print(revLst, lst)