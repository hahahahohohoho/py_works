x_arr = []
y_arr = []
result = []
for _ in range(3):
    x, y = map(int, input().split())
    x_arr.append(x)
    y_arr.append(y)
for x in x_arr:
    if x_arr.count(x) <2 :
        result.append(x)
for y in y_arr:
    if y_arr.count(y) <2 :
        result.append(y)
for i in result:
    print(i, end=" ")