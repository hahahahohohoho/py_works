# 예시 리스트
keys_list = ['a', 'b', 'c']
values_list = [1, 2, 3]

# 새로운 딕셔너리 생성
new_dict = {}

# 리스트의 길이가 같다고 가정하여 동일한 인덱스로 키와 값을 추출하여 새로운 딕셔너리에 추가
for i in range(min(len(keys_list), len(values_list))):
    new_dict[keys_list[i]] = values_list[i]

print(new_dict)
print(type(int(3)), 3)