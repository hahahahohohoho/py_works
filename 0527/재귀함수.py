def func(n) :
    if n == 1 :
        return '그렇습니다.'
    else :
        return '맞습니다.' + func(n)

print(func(2))