from itertools import combinations

arr = []
for _ in range(9) : 
    arr.append(int(input()))

for ncr in combinations(arr,7) :
    if sum(ncr) == 100 :
        for i in sorted(ncr):
            print(i)
        break