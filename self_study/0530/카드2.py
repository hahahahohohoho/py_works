N = int(input())
arr = [i for i in range(1, N+1)]
while(len(arr)>1):
    i=0
    tm = arr[i+1]
    arr.remove(arr[i])
    arr.remove(tm)
    arr.append(tm)
    i = i+1
for a in arr:
    print(a)