score = []
dic = {'A+' : 4.5,'A0':4.0,'B+' : 3.5,'B0':3.0,'C+' : 2.5,'C0':2.0,'D+' : 1.5,'D0':1.0,'F' : 0.0}
sum = 0
sum2 = 0
for _ in range(20):
    arr = input().split()
    b = float(arr[1])
    c = arr[2]
    if c != 'P' :
        sum += b * dic[c]
        sum2 += b
print(sum/sum2)





# P는 과목 계산에서 제외 필요