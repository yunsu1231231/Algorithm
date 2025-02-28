a = [1, 2, 3]

# 리스트 자체의 주소값
print(id(a))  # 리스트 객체 자체의 메모리 주소

# 각 요소의 주소값
print(id(a[0]))  # 첫 번째 요소 (1)의 메모리 주소
print(id(a[1]))  # 두 번째 요소 (2)의 메모리 주소
print(id(a[2]))  # 세 번째 요소 (3)의 메모리 주소

# 2004775422656
# 2004769859888
# 2004769859920
# 2004769859952