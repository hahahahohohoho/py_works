N=int(input())
sb = ba = pl = lim = 0
for _ in range(N):
    a, b = input().split()
    if a == 'STRAWBERRY' :
        sb += int(b)
    elif a == 'BANANA' :
        ba += int(b)
    elif a=='PLUM' :
        pl += int(b)
    else :
        lim += int(b)

if sb ==5 or ba ==5 or pl == 5 or lim ==5:
    print('YES')
else:
    print('NO')