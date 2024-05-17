a = str(input())
sum= len(a)
def toInt(a) :
    if a =='A' or a=='B' or a=='C' :
        return 2
    elif a =='D' or a=='E' or a=='F' :
        return 3
    elif a =='G' or a=='H' or a=='I' :
        return 4
    elif a =='J' or a=='K' or a=='L' :
        return 5
    elif a =='M' or a=='N' or a=='O' :
        return 6
    elif a =='P' or a=='Q' or a=='R' or a=='S' :
        return 7
    elif a =='T' or a=='U' or a=='V' :
        return 8
    else :
        return 9
for i in a :
    sum += toInt(i)
print(sum)