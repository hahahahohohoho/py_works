names = ['이창훈', '정형석', '임종태', '양한열']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(f"{names[0]} 안녕!")
print(f"{names[1]} 안녕!")
print(f"{names[2]} 안녕!")
print(f"{names[3]} 안녕!")

vh = ['자전거', '페라리', '오토바이']
print(f"나는 {vh[0]}를 갖고 싶습니다.")
print(f"나는 {vh[1]}를 갖고 싶습니다.")
print(f"나는 {vh[2]}를 갖고 싶습니다.")

customers = ['김', '박', '이', '최']
msg1 = '저녁 식사에 초대합니다.'
msg2 = '저녁 식사에 다시 초대합니다.'
print(f"{customers[0]} {msg1}")
print(f"{customers[1]} {msg1}")
print(f"{customers[2]} {msg1}")
print(f"{customers[3]} {msg1}")
customers.pop()
customers.append('한')
print(f"{customers[0]} {msg2}")
print(f"{customers[1]} {msg2}")
print(f"{customers[2]} {msg2}")
print(f"{customers[3]} {msg2}")
customers.insert(0, "양")
customers.insert(2, "노")
customers.insert(-1, "임")
msg3='더 큰 테이블을 찾았습니다.'
print(f"{customers[0]} {msg3}")
print(f"{customers[1]} {msg3}")
print(f"{customers[2]} {msg3}")
print(f"{customers[3]} {msg3}")
print(f"{customers[4]} {msg3}")
print(f"{customers[5]} {msg3}")
print(f"{customers[6]} {msg3}")

print(f"{customers[6]}, 죄송합니다.")
customers.pop()
print(f"{customers[5]}, 죄송합니다.")
customers.pop()
print(f"{customers[4]}, 죄송합니다.")
customers.pop()
print(f"{customers[3]}, 죄송합니다.")
customers.pop()
print(f"{customers[2]}, 죄송합니다.")
customers.pop()
print(f"{customers[0]}, {customers[1]} 초대가 취소되지 않았습니다.")
# del customers[0], customers[1]
# print(customers)

trip = ['Paris', 'Roma', 'London', 'New york', 'Tokyo']
print(trip)
sorted(trip)
print(trip)