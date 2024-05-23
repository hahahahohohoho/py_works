def cycle(num) :
    b = num % 10
    a = num // 10
    c = a+b
    result = b*10 + c%10
    return result

num1 = int(input())
num2 = cycle(num1)
result = 1
while num1 != num2:
    num2 = cycle(num2)
    result += 1
print(result)