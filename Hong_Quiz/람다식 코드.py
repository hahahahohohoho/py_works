#step 1
def ten_times(func): #func을 활용해서 함수를 파라미터로 전달받을 수 있음
    for i in range(10):
        func()
        
def print_hello():
    print('hello')

ten_times(print_hello)


#step 2
def add(x,y):
    return x+y

def apply_operation(operation, x, y): # operation 활용해서 operation의 파라미터와 함께 전달받을 수 있음.
    return operation(x, y)

result = apply_operation(add, 1, 2)
print(result)

# step 3
def power(item):
    return item**2
def under_tree(item):
    return item < 3
lst = [1,2,3,4,5]
map_list = map(power,lst)
print(list(map_list))
filter_list = filter(under_tree, lst)
print(list(filter_list))

# step 4 람다식
m_lst = map(lambda x:x**x, lst)
f_lst = filter(lambda x : x<3, lst)
print(list(m_lst))
