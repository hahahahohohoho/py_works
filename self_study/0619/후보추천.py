frame = int(input())
can = int(input())
arr = list(map(int, input().split()))
dic = {}
for i in arr :
    if i not in dic :
        if len(dic) < frame :
            dic[i] = 1
        else :
            ar1 = [k for k, v in dic.items() if v == min(dic.values())]
            del dic[ar1[0]]
            dic[i] = 1
    else :
        dic[i] +=1
key = dic.keys()
key = sorted(key)
print(*key)