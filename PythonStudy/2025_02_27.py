# Mutable = 가변 = 리스트, 딕셔너리, 집합 
# Immutable = 불변 = 정수, 실수, 문자열, 튜플 

# 자료형 
# 숫자, 문자열, 불, 변수, 리스트 ,튜플, 딕셔너리, 

# 숫자형
# 정수형, 실수형 # int, float 

a = 1.2
print(type(a)) # <class 'float'>

# 파이썬 모든 자료형은 객체로 저장 
# 예를 들어, a = 10이라면 숫자 10은 메모리의 특정 주소에 할당
# 이 객체는 참조를 통해 접근 
# a = 10이라면, a는 10이라는 객체가 저장된 메모리의 주소를 참조하는 변수

# 파이썬에서는 객체가 참조로 전달됩니다. 
# 즉, 변수를 다른 변수에 할당하거나 함수에 인자로 넘길 때, 객체 자체를 복사하는 것이 아니라 그 객체의 참조(주소값)가 전달
# 예를 들어, 리스트를 함수에 넘길 때, 리스트 객체 자체가 복사되지 않고 리스트 객체가 저장된 메모리 주소를 전달하게 됩니다. 
# 따라서 함수 내에서 객체를 수정하면, 원본 객체도 수정

a = 10
b = a  # a의 참조를 b에 전달

print(id(a))  # a의 메모리 주소
print(id(b))  # b의 메모리 주소

# 결과가 같다면 a와 b는 같은 객체를 참조하고 있다는 뜻

def modify_list(lst):
    lst.append(4)  # 리스트에 4를 추가

original_list = [1, 2, 3]  # 원본 리스트
print("Before function call:", original_list)

modify_list(original_list)  # 함수에 리스트를 넘김

print("After function call:", original_list)  # 함수 호출 후 리스트 출력

# 주소값이 복사 / 같은 메모리 상을 참조하게 됨 

# 제일 중요한 것은 파이썬은 모든 변수가 다 메모리에 저장 
#  a = 10이라면, 변수 a는 숫자 10 객체를 참조하는 변수입니다. 
#  즉, a는 10이라는 값을 가리키는 참조값

# 불변 객체 vs 가변 객체 
# 불변 객체 = 숫자, 문자열, 튜플 등이 불변 객체 = 값이 변경될 수 없다

# 불변 객체는 변수에 할당할 때, 
# 실제 객체의 복사본을 만드는 것이 아니라 참조를 전달합니다. 
# 그러나 불변 객체의 경우, 변수에 다시 할당하면 새로운 객체가 생성됩니다.

# 아 그니깐 불변 객체는 값을 변경하는 순간 값이 바뀔 수 없으므로 그냥 아예 메모리상에 새로운 객체가 생성 
# 자바 기준으로 return에 new가 붙었다고 생각하면 됨 

# 가변 객체는 값이 변경될 수 있는 객체입니다. 예를 들어, 리스트, 딕셔너리, 집합 등이 가변 객체

a = [1, 2, 3]  # 'a'는 리스트 객체를 참조
b = a  # 'b'도 같은 리스트 객체를 참조
print(id(a), id(b))  # 'a'와 'b'는 동일한 객체를 참조하므로 같은 id

b.append(4)  # 'b'에서 리스트를 수정
print(a)  # 'a'도 수정된 결과를 출력, 원본 리스트도 바뀌었음

# 변수가 저장하는 것은 객체 자체가 아니라 객체의 참조값입니다. 
# 즉, 변수가 참조하는 주소가 객체의 위치

# 파이썬에서 모든 것은 객체이기 때문에, 
# 타입도 클래스라는 객체로 취급되며, 객체는 항상 어떤 클래스의 인스턴스
# int는 클래스 객체이고, 그 클래스에서 만들어진 인스턴스가 a = 10입니다.


# 네, 정확합니다! 파이썬에서는 **상수(constant)**라는 개념이 언어적으로 존재하지 않습니다. 
# 대신, 모든 값은 객체로 취급되며, 이 객체가 가변인지 불변인지에 따라 동작이 달라진다.

# 가변객체
# list(리스트), dict(딕셔너리), set(집합), 바이트 배열

# 불변객체 
# int(정수), 부동소수점(float), 문자열(str), 튜플(tuple)

print(5/3)  # 나누기
print(5//3) # 몫
print(2**3) # 제곱 
print(7%3) # 나머지

# 문자열 = str 자료형 

a = "ac"
print(type(a)) # str 
print(a*3) # acacac 
len(a) # 파이썬에서 제공하는 함수 len -> class는? 

# \n -> 줄바꿈 문자 

# 문자열 슬라이싱
# a[::] # 이상 미만 간격
# a[::-2] # 거꾸로 

# 문자열 = immutable = 불변객체 

# 소수점 표현하기
# 0.4f -> 소숫점 4째자리까지 표현 

# 문자열 
a = 'hobby'
print(a.count('b')) # 2 

print(a.find('b')) #2 -> index 번호 찾기

a = ",".join('abcd') # a,b,c,d # 문자열 사이에 삽입
a = ",".join(['a','b','c']) # 리스트 사이에 삽입, 끝은 x 

a = "hi"
a.lstrip() # 왼쪽 공백 제거 
a.replace("ac", "bc") # ac 대신 bc로 교체 

a = "Life is too short"
a.split() # ['Life', 'is', 'too', 'short'] # 쪼개진 상태로 리스트가 나옴 

a.split(":") # :을 기준으로 나누기 

# 리스트 = 변수 여러개 담기
# 리스트의 주소값은? 

odd = [1,3,5,7,9]
type(odd) # <class, list>

e = [1,2,'life','is'] # 문자형 자료형, 숫자형 자료형 섞어서 한 번에 담을 수 있다
e = [1,[1,2],3] # 숫자형 자료형 

e[1][2] # 자바 기준으로는 체이닝 기법으로 주소값으로 접근인 듯 

# 문자열의 핵심은 문자열 자료형 

a[2:5] # 인덱싱 슬라이싱 

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

# 파이썬에서 서로 다른 자료형은 더할 수 없다 <-> TypeError
# str(3) -> 자료형 변환 

a[2:4] # -> 리스트 조작 **

# 리스트도 하나의 자료형니깐 함수가 존재 - 파이썬에서 모든 자료형, 변수는 객체

a = [1,2,3]
a.append(4) # [1,2,3,4]
a.append([5,7]) # 리스트가 추가 

a.sort() # 정렬 # 1,4,3 -> 1,3,4 # 문자열도 가능 
a.reverse() # 거꾸로 정렬 

a.sort().reverse() # 체이닝으로 주소값으로 계속 접근가능

a.index(3) # 3이 몇번째 index인지 반환하는 함수 

a.insert(0,4) # 0번째 인덱스에 값을 넣는 함수 

a.remove(3) # 첫번째 3인인 '값을' 제거 

a.pop() # 맨 끝에 있는 값을 날리기 -> return o
a.append(4) # 동작만 -> return x 

a.extend([4,5]) # 리스트에 리스트를 넣기 

# 리스트 = 서랍장 = 변수 여러가 한 번에 다루기

# 튜플 
# 튜플은 불변인 리스트 = 값을 다시 변경할 수 없다 

a = [1,2,3] # 파이썬에서 변수가 전부 객체라는게 # 지금 이 선언 자체가 new로 객체를 생성한 것 
a[3] = 3 # 이게 변경  

# 튜플 생성 
a = (1,2,3) # 생성 # 객체를 생성하는 것 <-> new가 생략 
a = 1,2,3 # 이것도 튜플 생성 가능 

#  차선에서 암기하고 + 이후 보충 
del a[0] # -> TypeError / 변경 불가능 

# 튜플 <-> 인덱싱, 슬라이싱 전부 가능 

# 튜플 -> 슬라이싱 -> 새로운 객체가 생성, return에 new가 있고 원래값은 그대로 존재 
# 이건 그냥 불변에서의 공통적 특징인 듯 

# 리스트에서 슬라이싱하면 -> 그 참조값의 가르키니는 메모리에 저장된 값이 그대로 저장된 형태 


a = [1,2,3] # 파이썬에서 변수가 전부 객체라는게 # 지금 이 선언 자체가 new로 객체를 생성한 것 
# 그래서 a class에 있는 함수를 a.으로 접근 가능 


# 딕셔너리 = 가변형 

# 딕셔너리 = Hash = Map = Objet = JSon 
# 키 벨류로 이루어진 자료형 
# {이름:"홍길동", 나이:"조윤수"} # key value 구조 

dic = {'name' : 'pey', 'color' : 'yellow'}
dic[2] = 'b' # key - value 추가
dic["key"] = 'value' # 맨 뒤에 추가 

del dic['name'] # 반환 x, 동작, key로 key - value 삭제 


# 딕셔너리 / key로 value를 얻기 

dic["key"] # key로 value를 찾기 # 반환 
# key는 중복 x 
# key에는 immutable 자료형만 사용가능 


dic = {'name' : 'pey', 'color' : 'yellow'}
print(list(dic.keys())) # keys() -> key들을 담은 dic.keys()

a.values() # 값들만 가져옴
a.items() # key,value가 튜플에 담겨져서 쭉 가져옴 

a.clear() # 값을 전부 날리기 

# 같은 기능 
dic["key"] # key 에러 
dic.get("key") # none 값 반환 

dic.get("key","값이 없을 때 반환")

print("name" in dic) # dic 안에 key 값으로 name이 있는자 -> true, false 반환 

# 집합 -> 자료형으로 제공 
# 집합에 관한 것을 쉽게 처리 
# set 

# 집합 생성 -> 기본적으로 객체 생성 = 집합은 가변 

a = set([1,2,3]) # {1,2,3} -> {} 인데 key, value가 아닌 값이 들어감 
print(a) 

# 집합은 -> 순서가 없고, 중복을 제거 
# -> 그래서 인덱싱 불가능
# -> 그래서 값을 가져오기 위해서는 list, tuple로 데이터 변환

# 그럼 집합을 사용하는 이유
# 중복제거, 교집합, 합집합 -> 함수로 제공 

s1 = set([1,2,3])
s2 = set([4,5,6])

# 교집합
print(s1 & s1)

# 합집합
print(s1 | s1)
print(s1.union(s2))

# 차집합
print(s1-s2)
print(s2.difference(s1)) # 인자로 전달 

# 집합에 값 추가 -> add 
s2.add(4)

# 업데이트 = 여러 값 한번에 추가
s1.update([4,4,5,6])

# 특정 값 제거 -> remove
s1.remove(2) # 인자로 전달이 인덱스가 아니라 값 

# bool / 참, 거짓 -> 맨 앞에 무조건 대문자 

# ==, < 등.. -> 논리연산자 사용가능

# 참, 거짓 
# 값이 없으면 -> 거짓 / 있으면 -> 참

print(bool([1,2,3])) # true 

# 변수

# 변수 = 주소값을 담는 것 / 메모리에 실제 값 = 객체 
# 주소값이 메모리 값을 참조하는 형태 

a = [1,2,3]
b = a # 주소깂이 복사 
a[1] = 4 

# 그래서 가변, 불변에 대한 이해 

a = [1,2,3]
b = a[0] # a[0] 자체가 새로운 객체를 반환
a[1] = 4 

a,b = ('python', 'life')
print(type(a)) 

a,b = ['python','life']

# 값 바꾸기 
a = 3
b = 5 
a,b = b,a # a,b 바꿀 수 있슴 

# 제어문
# 1. 조건문 2. 반복문

# 조건문(if문)
# if 조건문:
#   수행할_문장1
#   수행할_문장2 

# 들여쓰기를 잘못하면 <-> IndentationError 

# 조건안에 판단 -> and, or, not 


# in, not 

# in 

print(1 in [1,2,3]) # true 

# not

print(1 not in [1,2,3]) # false

print('a' in ('a','b','c')) 

#else a:
#    if:

# elif a: 

# 조건부 표현식 = 삼항연산자 
# message = "success" if score >= 60 else "failure"

# 있으면 참 / 없으면 거짓 -> 자주 사용 

# While 
a =  0
while a <10:
    a += 1 
    print("a")

# 디버깅 기능 -> 빨간 점 / break point / run -> start debuging / 한줄씩 실행 흐름 확인 

# while 문 강제로 빠져나가기 <- break 
# break 문은 현재 실행 중인 반복문(loop) = for,while,do-while 또는 switch문을 
# 즉시 종료하고 빠져나가는 역할

# 코드는 순차실행 <- 이게 대전제 
# continue 문은 현재 실행 중인 반복문의 나머지 코드를 건너뛰고,
# 다음 반복을 진행하는 역할

# for문 
# for 변수 in 리스트(또는 튜플, 문자열) = 값이 여러개인 것 

a = [(1,2),(3,4)]
for (first,last) in a:
    print(first+last) # (first,last) <- (1,2) # 각각 할당 

# 튜플은 굳이 감싸지 않아도 튜플 
for first,last in a:
    print(first+last)

# range
a = range(1,100) # [1,2,3,...99]


for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print('') # 개행의 역할 

# 기본적으로 print() 함수는 출력 후 줄바꿈을 자동으로 추가 = \n
# \n 대신에 띄어쓰기 # print(i*j, end=" ")

# 
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
    
# 리스트 컴프리헨션 
a = [1,2,3,4]
result = [num * 3 for num in a] # result list에 넣기 

# result = [num * 3 for num in a if num % 2 ==0] 

# 함수
# 반복 -> 덩어리로 묶기 /기능 단위로 분리 

def add(a,b): # add = 함수이름 / a,b 인자
    return a + b

add(1,2) # 반환 
print(add(1,2))

# 입력 x 
def say():
    return "Hi"

print(say()) # Hi

# return 값 x
def add(a,b):
    print(a+b)

a = add(1,2) # print 함수 동작 자체는 출력 = 3 

print(a) # 반환값이 없으므로 none

# 여러개의 매개변수를 한 번에 받을 수 있다. 
def add_many(*args):
    print(1)

# 여러값을 받을 수 있다. 
def print_keyValue(**kwagrs): 
    print(kwargs)


