a = input()

key_arr = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in range(len(key_arr)):
    a = a.replace(key_arr[i], '1')


print(len(a))