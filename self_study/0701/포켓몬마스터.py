import sys
input = sys.stdin.readline
N, M = map(int, input().split())
by_id, by_name = {}, {}
for i in range(1, N+1):
    pokemon = input().rstrip()
    by_id[i] = pokemon
    by_name[pokemon] = i
for _ in range(M) :
    a = input().rstrip()
    if a.isdigit():
        print(by_id[int(a)])
    else :
        print(by_name[a])