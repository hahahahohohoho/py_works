
#아래는 파이썬 세트를 사용하여 로또 복권 6개 번호와 보너스 번호를 100장 발행하여 세트에 저장하는 코드입니다.

import random
# 로또 복권 번호 생성 함수
def generate_lotto_numbers():
    # 1부터 45까지의 숫자 리스트 생성
    numbers = list(range(1, 46))
    
    # 무작위로 숫자 6개 선택하여 세트로 변환 (중복 없음)
    lotto_numbers = set(random.sample(numbers, 6))
    
    # 무작위로 숫자 1개 선택하여 보너스 번호 생성
    bonus_number = random.choice(numbers)
    
    return lotto_numbers, bonus_number

# 복권 리스트 만들기
lotto_list = []
def gen_lotto_list(num):
    for i in range(1, num+1):
        lotto_numbers, lotto_bonus_number = generate_lotto_numbers()
        #(복권번호, 보너스번호) 튜플로 저장
        lot_tuple = (lotto_numbers, lotto_bonus_number)    
        lotto_list.append(lot_tuple)
gen_lotto_list(3000)
    
# 당첨번호 만들기
winning_numbers, winning_bonus_number = generate_lotto_numbers()
print(f'당첨번호 : {winning_numbers}, 당첨 보너스 번호 : {winning_bonus_number}')

# #위너 체크 코드만들기
def check_winner(lotto_numbers, lotto_bonus_number, winning_numbers, winning_bonus_number):
    if len(lotto_numbers.intersection(winning_numbers)) == 6:
        if lotto_bonus_number == winning_bonus_number :
            return "1등" , lotto_numbers
        else :
            return "2등", lotto_numbers
    elif len(lotto_numbers & winning_numbers) == 5:
        if lotto_bonus_number == winning_bonus_number :
            return "3등", lotto_numbers
        else :
            return "4등", lotto_numbers
    elif len(lotto_numbers & winning_numbers) == 4:
        return "5등", lotto_numbers
    else :
        return f"꽝 {lotto_numbers} 맞은개수 : {len(lotto_numbers & winning_numbers)}"
    
i=1
for lotto_numbers, lotto_bonus_number in lotto_list:
    result = check_winner(lotto_numbers, lotto_bonus_number, winning_numbers, winning_bonus_number)
    print(f'{i}번째 : {result}')  
    i += 1
    
    
# for idx in range(1, 101):
#     #100장의 복권을 가져와 당첨번호 비교
#     check_winner(lotto_numbers, lotto_bonus_number, winning_numbers, winning_bonus_number, ind)