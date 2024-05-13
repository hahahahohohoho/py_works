data = [1, 2, 3, 3, 3]
print(data, type(data))

# data = [] #list()
# print(data, type(data))

print(data[0])
print(data[1])
print(data[2])
print(len(data))

data.append(6)
data.append(7)
data.append(8)
data.append(9)
data.append(10)
print(data, len(data))

data[3] = 4
data[4] = 5
print(data, len(data), sum(data), min(data), max(data))

data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
data = list(range(10, 0, -1))
print(data, type(data), sorted(data))

# 10
# 10 9 8 7 6 5 4 3 2 1
# 합계를 구하시오!, 정렬하시오!, 최댓값을 찾으시오!, 최솟값을 찾으시오!

# data = list(map(int, input().split()))
# print(data, type(data), type(data[0]))
# print(sum(data))

number = int('56')
print(number, type(number))


data = [1, 2, 3]
del data[1]
print(data)


data = [1, 2, 3, 4, 5]
print(data[len(data)-1])
print(data[::-1])