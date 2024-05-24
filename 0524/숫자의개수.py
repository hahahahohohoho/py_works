a, b, c = int(input()), int(input()), int(input())
to = str(a*b*c)
for i in range(10):
    print(to.count(str(i)))