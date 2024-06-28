import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dic = {}
for _ in range(N) :
    site, pw = input().split()
    dic[site] = pw
for _ in range(K):
    r_site = input().replace('\n', '')
    print(dic[r_site])