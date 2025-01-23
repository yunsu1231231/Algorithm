B,C,D = map(int,input().split())  # 주문한 버거 수, 사이드 메뉴 개수, 음료의 개수 

first = list(map(int,input().split()))
second =list(map(int,input().split()))  
third = list(map(int,input().split()))

first.sort(reverse=True)
second.sort(reverse=True)
third.sort(reverse=True)

minNumber = min(B,C,D) # 2 

total = 0
for i in range(minNumber):
    total += first[i] + second[i] + third[i]
totalDiscount = total * 0.9 # 할인 

firstSlice = first[2:]
secondSlice = second[2:]
thirdSlice = third[2:]

total_2 = 0 
for i in firstSlice[::1]:
    total_2 += i
for i in secondSlice[::1]:
    total_2 += i
for i in thirdSlice[::1]:
    total_2 += i

print(total+total_2)
print(int(totalDiscount+total_2))
