
#아래는 파이썬 세트를 사용하여 로또 복권 6개 번호와 보너스 번호를 100장 발행하여 세트에 저장하는 코드입니다.

import random

# 두 세트 생성
set1 = {1, 2, 3, 4, 5}
set2 = {3, 2, 1, 5, 4}

# 두 세트가 동일한지 확인 (모든 요소가 같은지)
# print("set1과 set2가 동일한지:", set1 == set2)

# 로또 복권 번호 생성 함수
def generate_lotto_numbers():
    # 1부터 45까지의 숫자 리스트 생성
    numbers = list(range(1, 46))
    
    # 무작위로 숫자 6개 선택하여 세트로 변환 (중복 없음)
    lotto_numbers = set(random.sample(numbers, 6))
    
    # 무작위로 숫자 1개 선택하여 보너스 번호 생성
    bonus_number = random.choice(numbers)
    
    return lotto_numbers, bonus_number

# 당첨 번호 생성
# winning_numbers, winning_bonus_number = generate_lotto_numbers()
# print("당첨 번호:", winning_numbers, "보너스 번호:", winning_bonus_number)

# 100장의 로또 번호 생성하여 당첨 여부 판별
# for idx in range(1, 101):
#     lotto_numbers, lotto_bonus_number = generate_lotto_numbers()
    
#     # 로또 번호와 보너스 번호가 당첨 번호와 일치하는지 확인
#     if lotto_numbers == winning_numbers and lotto_bonus_number == winning_bonus_number:
#         print(f"{idx}번째 로또 복권: 1등 당첨!")
#     elif lotto_numbers == winning_numbers:
#         print(f"{idx}번째 로또 복권: 2등 당첨! (보너스 번호 불일치)")
#     elif lotto_bonus_number == winning_bonus_number:
#         print(f"{idx}번째 로또 복권: 3등 당첨! (5개 일치 + 보너스 번호 일치)")
#     elif len(lotto_numbers.intersection(winning_numbers)) == 5:
#         print(f"{idx}번째 로또 복권: 4등 당첨! (5개 일치)")
#     elif len(lotto_numbers.intersection(winning_numbers)) == 4:
#         print(f"{idx}번째 로또 복권: 5등 당첨! (4개 일치)")
#     else:
#         print(f"{idx}번째 로또 복권: 꽝")
        
# step 1 당첨번호 생성
# step 2  100 장 복권을 발행할 때 마다 당첨 확인절차

#구현할것
# step 1 복권 100장 먼저 생성 후 저장(list로 저장 -> 오름차순 정렬)
lot = []
a = []
def lot_gen(num) :
    for _ in range(1, num+1) :
        lotto_numbers, lotto_bonus_number = generate_lotto_numbers()
        k = sorted(list(lotto_numbers))
        k.append(lotto_bonus_number)
        a.append(k)
lot_gen(1_000_000)
# step 2 당첨번호 생성
winning_numbers, winning_bonus_number = generate_lotto_numbers()
win = sorted(list(winning_numbers))
win.append(winning_bonus_number)
# step 3 당첨 확인

    # 7번째는 보너스 번호 
# for i in range(0, len(a)):





for i in range(0, len(a)):
    dang = []
    for j in win :
        if j in a[i] :            
            dang.append(j)
            if len(dang) == 7:
                print(f"{i+1}번째 로또 복권: 1등 당첨!")
            elif len(dang) == 6 :
                print(f"{i+1}번째 로또 복권: 2등 당첨!")
            elif len(dang) == 5 :
                print(f"{i+1}번째 로또 복권: 3등 당첨!")
            elif len(dang) == 4 :
                print(f"{i+1}번째 로또 복권: 4등 당첨!")
            elif len(dang) == 3 :
                print(f"{i+1}번째 로또 복권: 5등 당첨!")
            else :
                print(f"{i+1}번째 로또 복권: 꽝")


            
    # if len(same) == 6:
    #     print(f"{t+1}번째 로또 복권: 1등 당첨!")
    # elif len(same) == 5 :
    #     print(f"{t+1}번째 로또 복권: 2등 당첨!")
    # elif len(same) == 4 :
    #     print(f"{t+1}번째 로또 복권: 3등 당첨!")
    # elif len(same) == 3 :
    #     print(f"{t+1}번째 로또 복권: 4등 당첨!")
    # elif len(same) == 2 :
    #     print(f"{t+1}번째 로또 복권: 5등 당첨!")
    # else :
    #     print(f"{t+1}번째 로또 복권: 꽝")

    # if a[i] == win :
    #     print(f"{i+1}번째 로또 복권: 1등 당첨!")
    # # elif a[i].pop() == win.pop() :
    # #     print(f"{i}번째 로또 복권: 2등 당첨! (보너스 번호 불일치)")
    # else :
    #     print(f"{i+1}번째 로또 복권: 꽝")

        
    # a[i]와 sorted(win) 비교 해서 몇개인지 찾기