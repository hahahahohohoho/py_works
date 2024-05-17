S = str(input())

aList = [chr(i) for i in range(ord('a'),ord('z')+1)]

for al in aList :
    if al in S :
        print(S.find(al), end=" ")
    else :
        print(-1, end=" ")