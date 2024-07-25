N = int(input())

for _ in range(N):
    a, b = input().split()
    a = a.replace(b, '1')
    print(len(a))