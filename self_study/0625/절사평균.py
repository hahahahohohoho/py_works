import sys
N, K = map(int, sys.stdin.readline().split())
dic = {}
for i in range(N):
    dic[i] = float(sys.stdin.readline().replace("\n", ''))
    
sor_dic = sorted(dic.values())
for i in range(K) :
    del(sor_dic[0])
    sor_dic.pop()

def avg(lst) :
    av = sum(lst)/len(lst)
    return av

boj = sor_dic.copy()
for i in range(K):
    boj.insert(0, sor_dic[0])
    boj.append(sor_dic[-1])

print(round(avg(sor_dic),2))
print(round(avg(boj),2))

#부동소수점 문제로 풀지못함 ㅠ