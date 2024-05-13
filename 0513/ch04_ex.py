#4-1 피자
pizza = ['페페로니', '하와이안', '포테이토']
for d in pizza:
    print(f'나는 {d}피자가 좋습니다.')
print('나는 피자를 정말 사랑합니다.')

#4-2 동물
animal = ['강아지', '고양이', '토끼']
for d in animal:
    print(f'{d}는 정말 훌륭한 반려 동물입니다.')
print('이 동물들은 정말 귀엽습니다.')

#4-3 20까지 세기
for i in range(1, 21):
    print(i)

#4-4 백만
# for i in range(1, 1_000_001):
#     print(i)
    
#4-5 백만까지 더하기
a = list(range(1, 1_000_001))
print(max(a))
print(min(a))
print(sum(a))

#4-6 홀수
for i in range(1, 21, 2):
    print(i, end=" ")
print()
    
#4-7 333
for i in range(3, 31, 3):
    print(i, end=" ")
print()
    
#4-8 세제곱
for i in range(1, 11):
    print(i**3, end=" ")
print()

# 4-9 세제곱 내포
squares = [i**3 for i in range(1,11)]
print(squares)

# 4-10 슬라이스
animal = ['강아지', '고양이', '토끼', '소', '돼지', '원숭이', '닭']
print(f'리스트의 첫 세항목은: {animal[:3]}')
print(f'리스트의 중간 세 항목은: {animal[2:5]}')
print(f'리스트의 마지막 세항목은{animal[4:]}')

# 4-11 피자2
pizza.append('핫치킨')
friends_pizza= pizza.copy()
friends_pizza.append('고구마')
for p in pizza :
    print(f'내가 좋아하는 피자는 {p}피자')
for p in friends_pizza :
    print(f'친구가가 좋아하는 피자는 {p}피자')
