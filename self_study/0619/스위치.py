N = int(input())
switch = [-1]+list(map(int, input().split()))

def turn(n):
    if switch[n]==0:
        switch[n] =1
    else :
        switch[n] =0
def boy(n):
    for i in range(n, N+1, n):
        turn(i)
def girl(n) :
    turn(n)
    for k in range(N//2):
        if n + k > N or n-k <1 : break
        if switch[n+k] == switch[n-k]:
            turn(n+k)
            turn(n-k)
        else :
            break



M = int(input())
for i in range(M) :
    student, num = list(map(int, input().split()))
    if student == 1 :
        boy(num)
    else :
        girl(num)

for i in range(1, N+1) :
    print(switch[i], end=" ")
    if i%20 ==0 :
        print()