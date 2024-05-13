data = [1, 2, 3]
for d in data :
    print(d, end='')
# data[1] = 5
print('-',data[1])   
string = 'hello'
for s in string : 
    print(s, end='')
# string[1] = 'F' # string은 변경이 안된다.
print('-',string[1])

tup = (1, 2, 3) # 튜플
for i in tup :
    print(i)
# tup[1] = 5 # 튜플도 변경이 안된다.

data2 = [i**2 for i in data if i**2 <5]
print(data2, type(data2))

data3 = []
for i in data :
    data3.append(i**2)
print(data3)