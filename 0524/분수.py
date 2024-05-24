arr = [[] for __ in range(10)]
for i in range(1, 11):
    for j in range(1, 11):
        arr[i-1].append(f'{i}/{j}')
for i in arr :
    print(i, end='\n')

