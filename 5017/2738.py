A, B = map(int, input().split())

arr1, arr2 = [], []

for j in range(A):
        j = list(map(int, input().split()))
        arr1.append(j)
for j in range(A):
        j = list(map(int, input().split()))
        arr2.append(j)
for row in range(A):
        for col in range(B):
                print(arr1[row][col]+ arr2[row][col], end=' ')
        print()
        

