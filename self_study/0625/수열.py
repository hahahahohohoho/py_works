import sys
T, step = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

result = []
result.append(sum(arr[:step]))
for i in range(T-step):
    result.append(result[i] - arr[i] + arr[step+i])

print(max(result))
# 시간초과로 풀지 못함.....
#   해결 : sum을 for문 계속 반복하면 시간 복잡도 상승
#   규칙 활용을 위해 sum한번만 사용 후 앞에 값을 빼고 뒤에값을 더하는 형식으로 개선