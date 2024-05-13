a = int(input('첫번째 숫자를 입력하세요'))
b = input('두번째 숫자를 입력하세요')

for i in range(len(b), 0, -1) :
    print(a * int(b[i-1]))
print(a*int(b))