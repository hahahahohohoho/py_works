arr = []
for j in range(9):
        j = list(map(int, input().split()))
        arr.append(j)
max_arr = list(map(max, arr))
max_row = max_arr.index(max(max_arr))
print(max(max_arr))
print((max_row+1), arr[max_row].index(max(max_arr))+1)
