N = int(input())
string = input()
arr = [string[i:i+6] for i in range(0, len(string), 6)]
print(arr)