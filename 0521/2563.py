N = int(input())
c = []
for i in range(N):
    c.append(list(map(int, input().split())))
sum =0
for i in range(len(c)):
    for j in range(i+1, len(c)) :
        minX, maxX = min(c[i][0],c[j][0]), max(c[i][0],c[j][0])
        minY, maxY = min(c[i][1],c[j][1]), max(c[i][1],c[j][1])
        if minX+10 > maxX > minX :
            if minY+10> maxY > minY :
                w = minX+10 - maxX
                h = minY+10 - maxY
                sum += h*w
                print(sum)
        else:
            print('NO')
print(N*100 - sum)
            
            
        