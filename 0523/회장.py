N = int(input())
arr = [[] for __ in range(N)]

while True :
    a, b = map(int, input().split())
    if a == b == -1 :
        break
    else :
        arr[a-1].append(b-1)
        arr[b-1].append(a-1)

def score(arr1) :
    result = N - len(arr1)
    return result
score_arr = []
for i in arr :
    score_arr.append(score(i))
    
def func(lst, value):
    return [index + 1 for index, elem in enumerate(lst) if elem == value]
result = func(score_arr, min(score_arr))
print(min(score_arr), score_arr.count(min(score_arr)))
for i in result :
    print(i, end= ' ')