A, B = input().split()
Ar = int(''.join(reversed(A)))
Br = int(''.join(reversed(B)))

if Ar > Br :
    print(Ar)
else:
    print(Br)