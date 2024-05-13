score = 70
# if문은 else가 있어야 논리적 오류가 없음
if 90<= score < 100:
    print('A')
elif 80<= score < 90 :
    print('B')
else:
    print('F')
    #TODO
    #print('what?')
    
# if의 조건에는 str, int, list 다 들어간다 but 실수는 가능은 하지만 쓰지말자
# list 빈거는 거짓(false)
msg = 'hello'
if msg == 'hello':
    print('right!')
    
data = [1, 2, 3]
if 3 in data:
    print('Here!')
    
# 문자열 찾을 때 유용함!
string = 'Hello'
if 'He' in string :
    print('here!!')