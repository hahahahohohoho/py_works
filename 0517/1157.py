inp1 = str(input()).upper()
inp1_set = list(set(inp1))
cnt = []
for i in inp1_set :
    con = inp1.count
    cnt.append(con(i))
    
if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(inp1_set[(cnt.index(max(cnt)))])