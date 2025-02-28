#  순회할 수 있는(iterable) 자료형: list, tuple, set, dict, str, range, generator

# input()은 사용자의 입력을 문자열
# .split()은 기본적으로 공백(스페이스, 탭, 개행) 기준으로 문자열을 나눠 / 리스트를 반환

# (prompt: object = "", /) -> str
# prompt: object = "": 선택적으로 prompt 문자열을 받을 수 있음. 기본값은 빈 문자열("").
# /: 슬래시(/)는 해당 매개변수가 위치 전용(positional-only) 인자
# -> str: input()의 반환 타입은 str이라는 의미.

# a = input().split() 
# 13 3 4 ['13', '3', '4']

# d = map(int,input().split()) 
# 각 값을 int 타입으로 변환한 후 map 객체로 저장하는 과정을 포함합니다.
# <map object at 0x000001949E52D160> <class 'map'>
# 1. ['10', '20', '30']  # 문자열(str) 리스트
# 2. map(int, ...) → 리스트의 각 요소를 정수(int) 타입으로 변환
# 3. 반환되는 값은 map 객체이며, 즉시 리스트로 변환되지 않고 필요할 때 변환됨(이터레이터 특성).

# map은 이터레이터(iterator) 라서 한 번만 순회할 수 있음.
# map(int, ...)이 각 요소를 필요할 때마다(lazy evaluation) 정수로 변환
# 하지만, 아직 변환이 적용된 것은 아님!
# map 객체는 이터레이터(iterator) 이므로, 값을 필요로 할 때 변환을 실행
# 즉, 요소를 꺼낼 때(next() 호출 시) 비로소 변환이 수행됨!

# c = list(map(int,input().split())) 
# 리스트로 직접 변환

# 그럼 언제 map 객체를 쓰고 언제 list로 변환해서 사용하는지
# 1. 반복문에서 한 번만 사용 + sum(), max(), min() 함수 사용 -> map
# 2. 데이터 여러번 사용 / 인덱싱 / 정렬, 슬라이싱, 리스트 조작 
# 3. 그냥 input() 는 무조건 정수를 반환 

# 나누기, 몫, 제곱, 나머지
# print(3/5) 
# print(3//5)
# print(3**2)
# print(3%2)

# 문자열
# a = "I love basketball"
# print(len(a))
# print(a.count("b"))
# print(a.find("b"))
# c = a[::2] # 슬라이싱 -> 새로운 객체 생성 
# print(a)
# print(c)

# c = a.join(["me","too"])
# print(a) # 원본 보존 
# print(c) # # me too 사이에 a가 들어감 

# print("-".join(["i","love","basketball"])) # i-love-basketball
# print(type("-".join(["i","love","basketball"]))) # class, str 

# map(str, mixed_list)
# 각 요소를 str로 변환하는 이터레이터(iterator) 를 생성
# 이터레이터는 메모리에 모든 값을 저장하지 않음 → 즉, 한 번만 순회 가능!
# d = ["123", 1]
# print("-".join(map(str,d))) # 123-1

# .join() 메서드는 문자열 리스트를 결합하는 데 사용
# 즉, 리스트의 모든 요소가 문자열이어야 함.

# a = " say hoho a a "
# c = a[0:2:] # 새 객체를 반환 
# print(a.strip())
# print(a.lstrip())
# print(a.rstrip())

# 리스트 - 접근, 슬라이싱, 추가, 정렬, 거꾸로 정렬, 인덱스 반환, 제거, 리스트에 리스트 
# a = ["1","2",3]
# print(a[0]) 
# print(a[0:2])
# a.append(4) # 반환값 없이 리스트를 직접 조작 

# print(a.sort())
# a.sort() -> 반환값이 x 
# sorted(a) -> 이게 아마 반환값이 있는 듯 
# 숫자와 문자열이 섞여 있으면 정렬이 불가능 

# 반환값이 있다 = 원본이 보존된다"는 일반적으로 참이지만, 
# 가변 객체에서는 예외가 있으므로 메서드의 동작을 반드시 확인 

### 
# ✔ **가변 객체**: `list`, `dict`, `set`, `bytearray`, `deque`  
# ✔ **불변 객체**: `int`, `float`, `str`, `tuple`, `frozenset`, `bytes`  
# ✔ `tuple`은 불변! **가변 객체가 아님!**  
# ✔ `map()`은 데이터 타입이 아니라 이터레이터일 뿐 → 가변/불변 개념과 관련 없음. 

# a = ["1","2",3]

# for i in list(map(str,a)).sort():
#     print(i)
# sort()는 리스트를 직접 변경하지만(in-place), 반환값이 None이므로 for 문에서 사용할 수 없음.    

# a = ["1","2",3]
# sorted= list(map(str,a)).sort() # 반환이 없으면 받을수도 없고 -> Null이 저장되는구나
# for i in sorted:
#     print(i)

# sort()는 반환값이 없기 때문에 map()과 직접 결합해서 사용할 수 없어
# map()을 list()로 변환한 후 sort()를 호출하면 순회할 방법이 사라지고, None을 저장하는 꼴

# a = ["1","2",3]
# sorted= sorted(list(map(str,a))) 
# for i in sorted:
#     print(i)


# 1. map(str, a)는 이터레이터(iterator) 객체를 반환
# 2. sort()는 리스트(list) 객체에서만 사용 가능하고, map 객체에서는 사용할 수 없음.

# print(a.sort().reverse())
# print(a.find("1"))
# print(a.remove("1"))
# print(a.extend([1,2,3]))

# 오류 메세지 구조
# 오류 발생 위치 → 오류가 발생한 파일과 줄 번호
# 오류 유형 및 원인 → IndentationError: unexpected indent ex. 예상치 못한 들여쓰기가 있다는 의미

# 리스트에 리스트 추가 
# a= ["a","b",3]
# a.extend([3,4])
# print(a)

# append()는 "하나의 원소"를 리스트 끝에 추가
# extend()는 "리스트를 펼쳐서" 추가
# extend()는 리스트뿐만 아니라 튜플, 문자열 같은 iterable도 펼쳐서 추가할 수 있음. / 순회 가능한 객체에기만 하면 됨 / 굳이 iterator일 필요는 x 

# 튜플 생성
a = 1,2,3
b = (1,2,3)

# print(1 in a) True
# print(2 not in b) False

# 딕셔너리 - 추가, 삭제, 찾기, 값들만 가져오기, key만 가져오기, dic 안에 값이 있는지 없는지 -> 딕셔너리에만 사용? 
c = {"subject":"math", "age":"17","height":"110"}

# c["see"] = "17" # 리스트랑 똑같이 []로 접근하고 추가 
# del c["height"]
# print("subject" in c) # True
# print(list(c.values())) # 동작 -> 함수 -> () # dict_values(['math', '17', '110']) / dict_values 라는 type이 나오네 
# dict_values는 dict_values 타입의 객체이며, 딕셔너리의 값들(values())을 저장하는 특수한 객체
# dict_values는 이터러블(Iterable)
# dict_values는 이터러블이므로 for 문에서 사용 가능.

# print(c)
# print(type(c))
# print(list(c))

# print(c.keys()) # dic_keys 자료형으로, key값만 
# print(list(c.keys())) # 리스트
# print("subject" in c.keys()) # True

# 리스트안에 튜플 순회
# a = [(1,2),(2,3),(3,4)]
# for (first,second) in a:
#     a = first 
#     b = second 
#     print(a)
#     print(b)
    
# set 함수 / 중복 x, 순서 x 
# a = set([1,2,3,2,2])
# print(a)

# b = {1,2,3,3,3,3,}
# print(b)

# range - 개행 
a = [1,2,3,4]
for i in a:
    print(i,end=",")
print("")
print("확인")

# 리스트 컴프리헨션 

# squares = [x**2 for x in range(1, 6)]  # 1부터 5까지의 제곱을 리스트로 생성 # 본문에 들어갈 조건이 for문 앞에 
# print(squares)  # 출력: [1, 4, 9, 16, 25]

# squares = []  # 빈 리스트 생성
# for x in range(1, 6):  # 1부터 5까지 반복
#     squares.append(x**2)  # x의 제곱을 리스트에 추가
# print(squares)  # 출력: [1, 4, 9, 16, 25]

