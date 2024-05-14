import random

def generate_winning_numbers():
    winning_numbers = set()
    while len(winning_numbers) < 6:
        winning_numbers.add(random.randint(1, 45))
    return sorted(list(winning_numbers))

def generate_bonus_number():
    return random.randint(1, 45)

def generate_lotto_numbers():
    lotto_numbers = set()
    while len(lotto_numbers) < 6:
        lotto_numbers.add(random.randint(1, 45))
    return sorted(list(lotto_numbers))

def check_result(user_numbers, winning_numbers, bonus_number):
    matched_numbers = set(user_numbers) & set(winning_numbers) # 교집합
    num_matched = len(matched_numbers)
    if num_matched == 6: # 교집합의 길이가 6이면
        if bonus_number in user_numbers: # 보너스도 맞으면 
            return "1등" 
        else:
            return "2등"
    elif num_matched == 5:
        if bonus_number in user_numbers:
            return "3등"
        else:
            return "4등"
    elif num_matched == 4:
        return "5등"
    else:
        return "꽝"

def main():
    print("로또 복권 프로그램에 오신 것을 환영합니다!")
    
    # 당첨 번호 생성
    winning_numbers = generate_winning_numbers()
    bonus_number = generate_bonus_number()
    print("당첨 번호:", winning_numbers)
    print("보너스 번호:", bonus_number)
    
    # 로또 수 입력 받기
    num_lottos = int(input("구매할 로또 수를 입력하세요: "))
    
    # 각 로또에 대해 결과 확인
    for i in range(num_lottos):
        user_numbers = generate_lotto_numbers()
        result = check_result(user_numbers, winning_numbers, bonus_number)
        print(f"{i+1}번째 로또 결과:", result)

if __name__ == "__main__": #main문 설정
    main()
