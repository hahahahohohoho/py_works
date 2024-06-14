N = int(input())

for _ in range(N):
    inp = input()
    res = []
    check = False
    for i in inp:
        if i == '(':
            res.append(i)
        elif i ==')' :
            if not res :
                check = True
                break
            res.pop()
    if res or check :
        print('NO')
    else :
        print('YES')