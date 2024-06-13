# lst형태는 하는데 오래걸림 해쉬맵(딕셔너리) 구조로 사용
# N = int(input())
# lst=[]
# for _ in range(N):
#     a = input().split()
#     if a[1] == 'enter':
#         lst.append(a[0])
#     elif a[1] == 'leave':
#         lst.remove(a[0])
# for i in sorted(lst, reverse=True) :
#     print(i)

import sys


n = int(sys.stdin.readline())
temp = dict() # 딕셔너리 형

# 반복문을 통해 출입 기록울 확인한다.
for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())

    # 출입을 했으면 딕셔너리로 받는다.
    if b == "enter":
        temp[a] = b
        print(temp)
    # 퇴근을 했으면 삭제해준다.
    else:
        del temp[a]

# 이름(temp.keys())을 사전 순의 역순으로 정렬한다.
temp = sorted(temp.keys(), reverse=True)

for i in temp:
    print(i)