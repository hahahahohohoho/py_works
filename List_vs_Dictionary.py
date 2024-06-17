import time
import random

'''
## Dictionary과 List에서 탐색의 성능 비교 ##

- 비교 상황 key 값이 n(0~1000000) 인
value를 찾는 시간을 비교

조건 1. list와 dict의 key와 value는 동일
조건 2. list와 dict에 값을 넣는 순서 동일
조건 3. key값은 중복없이 랜덤(0~1000000)
조건 4. value는 랜덤(0~100)

'''
#1. 랜덤 값 생성
def create_data (n):
    # key 값 생성
    keys = [i for i in range(n)]
    # key 값 섞기 (중복없는 랜덤)
    random.shuffle(keys)
    # value값 생성 
    # random.randrange(시작, 끝) -> 범위 내 랜덤 출력
    values = [random.randrange(0,100) for i in range(n)]
    
    # 두가지 데이터로 [key, value] array를 생성
    data = [[keys[i],values[i]] for i in range(n)]
    #print(data)
    return data 

def create_dict (li):
    d = {}
    KEY = 0
    VALUE = 1
    #랜덤값을 딕셔너리에 대입
    
    for i in li:
        d[i[KEY]] = i[VALUE]
    #print(d) 
    return d

def find_list(key, li):
    start = time.time()
    for i in li:
        if i[0] == key:
            t = (time.time() - start) * 1000 #ms
            return {'key': i[0] ,'value': i[1], 'time' : t}
    return -1

def find_dict(key, d):
    start = time.time()
    try:
        value = d[key]
        t = (time.time() - start) * 1000 #ms
        return {'key': key ,'value': value, 'time' : t}
    except:
        return -1

def time_test(n, key):
    # 리스트 생성
    NUM_DATA = n # n개의 데이터
    KEY = key # 찾으려는 Key 값
    li = create_data(NUM_DATA)

    # 딕셔너리 생성
    d = create_dict(li)
    #시간 측정(리스트)
    t_li = find_list(KEY, li)
    #시간 측정(딕셔너리)
    t_d = find_dict(KEY, d)
    
    return {'list': t_li, 'dict': t_d}

if __name__ == '__main__':

    print('[10개 탐색 시]')
    r = time_test(10, 1)
    print(f'리스트 탐색: {r["list"]}')
    print(f'딕셔너리 탐색: {r["dict"]}')
    print(f'{r["list"]["time"] / r["dict"]["time"]}배 차이\n')
    
    print('[10^2개 탐색 시]')
    r = time_test(100, 1)
    print(f'리스트 탐색: {r["list"]}')
    print(f'딕셔너리 탐색: {r["dict"]}')
    print(f'{r["list"]["time"] / r["dict"]["time"]}배 차이\n')

    print('[10^4개 탐색 시]')
    r = time_test(10000, 1)
    print(f'리스트 탐색: {r["list"]}')
    print(f'딕셔너리 탐색: {r["dict"]}')
    print(f'{r["list"]["time"] / r["dict"]["time"]}배 차이\n')

    print('[10^6개 탐색 시')
    r = time_test(1000000, 1)
    print(f'리스트 탐색: {r["list"]}')
    print(f'딕셔너리 탐색: {r["dict"]}')
    print(f'{r["list"]["time"] / r["dict"]["time"]}배 차이\n')