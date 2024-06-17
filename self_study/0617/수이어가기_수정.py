def check(a, b) :
    n_list = [a, b]
    while True :
        num = a-b
        if num < 0:
            break
        n_list.append(num)
        a= b
        b= num
    return n_list

fir = int(input())
sec = fir
max_list = []
while True :
    cnt = check(fir, sec)
    if len(max_list) < len(cnt) :
        max_list = cnt
    sec -= 1
    if sec < 0 :
        break
print(len(max_list))
print(*max_list)