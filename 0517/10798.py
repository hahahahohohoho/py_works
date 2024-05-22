arr = []
length = []
for _ in range(5):
    j = list(input())
    arr.append(j)
    length.append(len(j))

rst = ''
for i in range(max(length)):
    for j in range(len(arr)) :
        if i < length[j]:
            rst += arr[j][i]
print(rst)