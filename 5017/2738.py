A, B = map(int, input().split())

arr1 = []
arr2 = []
for j in range(A):
        arr1.append(list(map(int, input().split())))
print(arr1)
for j in range(A):
        arr2.append(list(map(int, input().split())))
print(arr2)
sum=0
sumArr=[]
for j in range(A):
    for i in range(B) :
        sum = arr1[j][i] + arr2[j][i]
        print(sum, end=' ')
    print()
