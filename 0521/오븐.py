h, m = map(int, input().split())
m1 = int(input())
m2 = m+m1 

if m2<60 :
    print(h, m2)
elif m2 >= 60 :
    if h+int(m2/60) <24 :
        print(h+int(m2/60), m2%60)
    else :
        print(h+int(m2/60)-24, m2%60)