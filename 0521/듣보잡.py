n, m = map(int,(input().split()))
noL, noS = set(), set()
for i in range(n) :
    noL.add(input())
for i in range(m) :
    noS.add(input())
result = sorted(list(noL&noS))
print(len(result))
for i in result :
    print(i)
