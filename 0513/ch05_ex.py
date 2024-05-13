#5-3 외계인 색깔 #1
alien_color = 'yellow'
if alien_color =='green':
    print('플레이어가 5점을 획득했습니다.')


#5-4 외계인 색깔 #2
if alien_color =='green':
    print('플레이어가 5점을 획득했습니다.')
else : 
    print('플레이어가 10점을 획득했습니다.')
#5-5 외계인 색깔 #3
if alien_color =='green':
    print('플레이어가 5점을 획득했습니다.')
elif alien_color =='yellow' : 
    print('플레이어가 10점을 획득했습니다.')
elif alien_color =='red' : 
    print('플레이어가 15점을 획득했습니다.')

#5-6 삶의 단계
age = 65
if age < 2 :
    print('baby')
elif 2<= age < 4 :
    print('toddler')
elif 4<= age < 13 :
    print('kid')
elif 13<= age < 20 :
    print('teenager')
elif 20<= age < 65 :
    print('adult')
elif 65 <=age :
    print('elder')
    
    
#5-7 좋아하는 과일
favorite_fruit = ['수박', '복숭아', '사과']

if '수박' in favorite_fruit :
    print('당신을 정말 수박을 좋아하네요!')
if '당근' in favorite_fruit :
    print('당신을 정말 당근을 좋아하네요!')
if '토마토' in favorite_fruit :
    print('당신을 정말 토마토를 좋아하네요!')
if '복숭아' in favorite_fruit :
    print('당신을 정말 복숭아를 좋아하네요!')
if '딸기' in favorite_fruit :
    print('당신을 정말 딸기를 좋아하네요!')
    
#5-8 관리자
user = ['a', 'b', 'c', 'd', 'admin_e']
for id in user :
    if 'admin' in id :
        print('관리자님 안녕하세요')
    else :
        print(f'{id}님 안녕하세요')
        
#5-9 사용자 없음
# del user[:]
if user == []:
    print('사용자가 있어야합니다.')
    
#5-10 사용자 이름체크
current_users = ['Jason', 'MJ', 'Tom', 'Al', 'Jo', 'Kim']
new_users = ['Kim', 'Mj', 'Choi', 'Yang', 'Koo']

for id in new_users :
    if id in current_users :
        print(f'{id}이 중복입니다. 새로운 사용자 이름을 입력하세요')
    else :
        print(f'{id}는 사용할 수 있습니다.')

#5-11 서수
a = 1
if a == 1:
    print(f'{a}st')
if a == 2:
    print(f'{a}nd')
if a == 3:
    print(f'{a}rd')
elif a > 3 :
    print(f'{a}th')