# N = int(input())

def func(a, b) :
    res = a-b
    if res > 0 :
        print(res, end= " ")
        func(b, res)
    else : 
        0
print(func(100,62))