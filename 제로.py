import sys
imput = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N) :
    a = int(input())
    if a == 0 :
        lst.pop()
    else :
        lst.append(a)
print(sum(lst))