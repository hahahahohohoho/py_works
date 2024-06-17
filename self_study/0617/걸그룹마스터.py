N, M = map(int, input().split())
dic = {}
for _ in range(N):
    team = input()
    b= int(input())
    dic[team] = []
    for _ in range(b):
        dic[team].append(input())
    dic[team] = sorted(dic[team])
for _ in range(M) :
    inp = input()
    typ = int(input())
    if typ == 0 :
        arr = dic[inp]
        for k in arr :
            print(k)
    else :
        val = list(dic.values())
        key = list(dic.keys())
        for j in range(N) :
            if inp in val[j]:
                print(key[j])