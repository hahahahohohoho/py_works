arr1, arr2 = [],[]
for _ in range(10):
    arr1.append(int(input()))
for _ in range(10):
    arr2.append(int(input()))
arr1.sort(reverse=True) 
arr2.sort(reverse=True)
sum1, sum2 = 0, 0
for i in range(3):
    sum1 += arr1[i]
    sum2 += arr2[i]
print(sum1, sum2)