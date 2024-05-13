# print("hello, world!")
# age = 5
# fi = 3.14
# msg = 'hello, world!'
# mask = 'everything' or 'object'
# data = [1, 2, 3]
# print(type(age), type(fi), type(msg), type(data), type(mask))

def calc(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a//b) # 몫
    print(a**b)
# a=1
# b=2
# calc(a,b)


# swap
# temp = a
# a= b
# b= temp
# python
a, b = 3.14, 1_000_000_000
b, a = a, b

# print(a, b)

msg = 'hello, world!'
print(msg)
#str은 배열처럼 쓸 수 있다.
print(msg[0])
print(msg[1])
# msg[0] = 'H'
# 하지만 하나씩 대입연산은되지 않는다.


a = 'hello'
b= 'world'
print(f'{a},{b}! \n\thahahaha!')