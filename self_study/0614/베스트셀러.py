N = int(input())
dic = {}
for _ in range(N):
    a= input()
    if a in dic :
        dic[a] +=  1
    else :
        dic[a] = 1
num = max(dic.values()) # max값을 num에 저장하고
lst = []
for i in dic :
    if num == dic[i] : # max값과 같은 key들을 lst에 저장
        lst.append(i)
lst.sort() # lst 를 오름차순으로 정렬
print(lst[0]) # 제일앞에 있는 하나만 출력
