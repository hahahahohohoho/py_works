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

for _ in range(10): #range(a,b)는 a보다 크거나 같고 b보다 작은 수
    #for문을 10번 돌리고 싶으면 for i in range(10)
    print('a', end = ' ')

# index 값 불러오기
for idx, d in enumerate(data) : 
    print(idx, d)
    
data_2d = [[1, 2, 3],
           [4, 5, 6]]

#이중 for문
for data in data_2d :
    for d in data:
        print(d, end= ' ')
    print()
    
# 구구단(이중 for문 예제)
for i in range(1, 10) :
    for j in range(1,10) :
        print(f'{i} x {j} = {i*j}')  # f스트링에 익숙해지기!
    print()

data = [1, 3.14, 'hello', max, range]
for d in data:
    print(d, type(d))
    print('next')
# (↑) 파이썬스럽게 코딩하라! 
# for i in range(len(data)) :
#     print(data[i], type(data[i]))

# data = range(1, 1001)
#range만으로는 list가 안됨 만들고 싶으면 list(range(1, 1001))
# print(data, type(data))


# data = list(range(1, 11))
# print(data[1:-1], print(data[:5]), print(data[5:]), sep='\n')
# print(data, data[::-1], sorted(data, reverse='True'), sep='\n')

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b
    # a, b = b, a
    
a, b = 1, 5
print(a, b)
a, b = swap(a, b)
print(a, b)

data = [1, 2, 3]
data2 = data.copy()
#그냥 대입하면 외래키 마냥 하나바꾸면 다바뀜
#리스트 오류가 발생하면 리스트를 튜플로 바꿔보자
data2[1] = 5
print(data, data2, sep='\n')