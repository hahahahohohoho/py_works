# 비교대상
compare_targets = [({35, 8, 11, 13, 45, 19}, 25), ({32, 1, 3, 35, 37, 28}, 28), ({3, 41, 13, 14, 29, 30}, 4)]

# 비교군
comparison_group = {41, 9, 11, 19, 26, 31}

# 교집합을 저장할 빈 리스트 생성
intersection_results = []

# 각 비교대상에 대해 반복하여 교집합을 구함
for target_set, comparison_value in compare_targets:
    # 비교대상의 셋과 비교군의 셋의 교집합을 구하고 리스트에 추가
    print(target_set, type(target_set))
    intersection = target_set.intersection(comparison_group)
    intersection_results.append(intersection)

print(intersection_results)
