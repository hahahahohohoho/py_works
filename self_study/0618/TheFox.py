import sys
N=int(input())

for i in range(N):
    arr = sys.stdin.readline().split()
    dic = {}
    while True :
        a = sys.stdin.readline().replace('\n', '')
        if a == "what does the fox say?" :
            break
        animal = a.split()
        dic[animal[0]] = animal[2]
    val = dic.values()
    arr = [i for i in arr if i not in val] #removeall 쓰는법
    print(*arr)