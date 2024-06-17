import sys
input = sys.stdin.readline()
N = int(input)

def func(a, b, arr) :    
    if a >b :
        arr.append(a-b)
        func(b, a-b, arr)
    return arr


res, max_len = [], 1

for i in range(N) :
    arr = [N,i]
    func(N, i, arr)
    if max_len < len(arr) :
        max_len = len(arr)
        res = arr
        
# 결과출력
print(max_len)
print(*res)