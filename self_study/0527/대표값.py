lst = []
for _ in range(5):
    lst.append(int(input()))
lst = sorted(lst)
sum = 0
for i in lst :
    sum = sum + i
print(int(sum/5))
print(lst[2])