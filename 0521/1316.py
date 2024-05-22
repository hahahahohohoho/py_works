# N = int(input())

# for _ in range(N):
    # A = input()
a= 'happy'
k = ''
for i in range(1, len(a)):
    if a[i-1] == a[i] :
        k = a.replace(a[i], '')
print(k)
