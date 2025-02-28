# https://www.youtube.com/watch?v=ftQZo7XaTOA&t=22s
# 4:33:81부터

# 함수

def sub(a,b):
    return a-b

# key - value / 딕셔너리 

def add_mul(a,b):
    return a+b, a*b # 튜플 형태로 반환


a = 1 # 전역
def art(a):
    a = a + 1 # a 상자는 지역변수  
print(a)

# return -> 바깥 값 변경 + 저장
a = 1 # 전역
def art(a):
    a = a + 1 # a 상자는 지역변수
    return a  
print(art(a))

# Immutable = 정수,실수,문자열,튜플
a = 1 
def vartest(a):
    a = a + 1
vertest(a)
print(a)
    
# Mutable = 리스트,딕셔너리,집합
b = [1,2,3]
def vartest2(b):
    b = b.append(4) # b.append(4) <- 리스트 자체가 변화 / return x, 동작 
vartest2(b)
print(b)

# lambda = 익명함수 

def add(a,b):
    return a+b

add = lambda a,b:a+b # 앞 인자, 뒷 return 값 

# 사용자 입출력 

# input 입력은 기본 str 

a = input()

print("life", "is") # 띄어쓰기로 출력

for i in range(10):
    print(i, end= '') # \n 대신에 공백, 공백으로 연결 / 마지막은 제외 
    
# 클래스

# 클래스 -> 실제 생성해서 메모리에 할당 = 객체 = 변수, 함수
# 클래스 -> 대문자
# 객체 = 인스턴스 / 엄밀히 구분 x 

# pass? 

# 필드 선언은 필요 없는건가? 
# 파이썬에서는 __init__() 메서드에서 인자로 받은 값들이 자동으로 필드(즉, 인스턴스 속성)로 생성됩니다. 
# 이때, 인자로 받은 값은 해당 클래스의 인스턴스에 속하는 필드로 할당됩니다.

class Cookie:
    def __init__(self): # 생성자 = 인스턴스 생성할 때 무조건 실행 
        self
        
    def setdata(self,first,second): # self = this 
        self.first = first
        self.second =second 

초코쿠키 = Cookie() # 리턴으로 객체 생성 / Class = type 
아몬드쿠키 = Cookie() 

# 클래스 자체에서 함수를 호출하도 가능 /self 생략가능
# 자바 static 메서드랑 유사 

a = Calss()
Calss.setdata(a,4,5) 

a.first() # 객체에 있는 변수 

# 객체는 변수를 각각 가지고 있고 함수는 공유 

# 클래스의 상속 

class FourCal:
    
# class에 인자로 넘겨줘서 상속 
class MoreFourCal(FourCal):
    pass

# 클래스변수 = 자바에서 static 변수
# static 변수는 인스턴스를 생성하지 않고 클래스 이름을 통해 접근

# 모듈 = 파일을 불러와서 쓰는 개념 # ex. mod1.py 
from mod1 import add # add만 가져오기 
print(add(3,4)) # add 바로 사용 가능 

# __main__ <- 예약어 

# 모듈 자체를 실행할때만 실행 
if __name__ == "__main__":
    print(add(1,2))

# 모듈안에 클래스, 변수, 함수 포함 가능 

# 하나씩 짚으면서 / a 

# 패키지 = 모듈을 넣어놓은 디렉토리 집합 

# init -> 패키지에서 생성자 

from game.sound import *

import mod3 as m

m.add()

# 내장함수 = ex. print -> 패키지를 import 안해줘도 되는건가 

# enumerate / 리스트를 딕셔너리 처럼 사용 

# 표준 라이브러리 = import 해서 사용 / 따로 설치 x 

import datetime
day1 = datetime.date(2021,12,14)

print(type(day1)) # <class,'datetime.date'> # datetime.date 클래스 

# 외부 라이브러리 = 다른 사람이 외부에서 만들어놓은 라이브러리
# pip install 패키지이름 
# PIPY -> 사용법 # 공식문서, 구글링, chatgpt 

# from faker import Faker # Faker = class

from fake import Faker
fake = Faker()

fake.name()
fake.address()
fake.text()

# 프로그램 사고 
# 1. 입, 출력 // 함수, 입력, 출력 
# 2. 결과 어떻게 저장하지? -> 연속된 자료형 = 리스트 
# 3. 반복되는 부분 -> 반복문으로 변경 
# 4. 문장 -> 조건별로 끊어서 -> 어떻게 구할지 


# 7장 

# 인코딩 / 문자열 -> byte 변환 (type = byte)
# 디코딩 / byte -> 문자열 변환 
# 인코딩 된 방식으로 디코딩을 해야 됨 

# 클로저 = 함수안의 함수 
# 함수를 통으로 return

# 데코레이터 = 시간 측정 

# 이터레이터, 제너레이터 

# 이터레이터 = 반복 가능한 객체 + next() 사용 가능  
for a in [1,2,3]:
    print(a)

iter(a) # 자료형 변환 

# 제너레이터 = 이터레이터를 생성하는 함수 // 실행할 때마다 메모리에 올림 
# 호출될 때마다 실행 = lazy evaluation

# 파이썬 타입 어노테이션
# 변수와 함수에 타입을 지정가능 

# 프로그램 실행중에 타입이 변경가능 -> 동적

# 지정한 타입 외의 다른 타입을 넣으면 -> 컴파일 오류 -> 정적 // ex. 정적 

# 정규 표현식 = 정규식 
# 특정 패턴을 찾는 것 

# 경로에 대한 부분이지 / 클래스 생성해서 주소값을 참조해서 . <- 으로 접근하는 것이랑 구분 
# 모듈, 패키지, 라이브러리, 정리
# 라이브러리 = 모듈 or 패키지 
# 외부 라이브러리, 내부 라이브러리 

# 모듈 = 파일 

# import 방법의 차이

# from mod1 import add  # add 함수만 가져옴 # 특정 함수(변수, 클래스)를 직접 가져
# print(add(3, 4)) 
# add(3, 4)처럼 모듈 이름 없이 바로 함수를 사용

# import mod1  # 전체 모듈 가져오기
# print(mod1.sub(7, 3))  
# mod1.sub처럼 모듈 이름을 붙여서 접근

# 패키지 = 모듈을 모아놓은 디렉토리(폴더) 구조

# game/
#  ├── __init__.py  # 패키지 초기화 파일 (필수)
# ├── sound/
# │    ├── __init__.py
# │    ├── effects.py
# ├── graphics/
#      ├── __init__.py
#      ├── render.py

# 패캐지 사용하기 
# from game.sound import effects  # 특정 모듈 가져오기
# from game.sound.effects import echo  # 특정 함수 가져오기

# from game.sound.effects import echo  # effects 모듈 안에서 echo 함수만 가져옴
# echo()  # 모듈명을 생략하고 바로 사용 가능

# import는 모듈 내에 존재하는 모든 객체(함수, 클래스, 변수 등)를 가져올 수 있음

# # 사용 예시

# from game.sound import effects  # effects 모듈 전체 가져오기
# effects.some_function()  # effects 안에 있는 some_function() 호출

# 특정 함수만 가져오기
# from game.sound.effects import echo  
# echo()  # "Echo function 실행!"

# 특정 클래스 가져오기
# from game.sound.effects import SoundEffect  
# se = SoundEffect()
# se.play()  # "SoundEffect 실행!"

# 특정 변수 가져오기
# from game.sound.effects import volume  
# print(volume)  # 10


# from 뒤에는 "패키지" 또는 "모듈"이 올 수 있다
# import 뒤에는 "모듈" 또는 "모듈 안의 특정 객체(함수, 클래스, 변수)"가 올 수 있다

# from game.sound import effects  # 패키지(game.sound)에서 모듈(effects) 가져오기 # 모듈 import 
# effects.echo()  # 사용 가능

# from game.sound.effects import echo  # 함수 import 
# echo()  # 사용 가능

# -> 결국 둘 사이에 사용 차이가 발생하는 이유는 경로의 차이 / 객체를 통한 함수, 변수의 접근과는 별개 
# 패키지 = 폴더 / 모듈 = 파일

# 라이브러리(Library)는 특정 기능을 제공하는 코드 묶음을 의미
# 라이브러리 = 모듈일 수도 있고, 패키지일 수도 있다. 

# 라이브러리가 단일 파일(.py 파일 하나)로 되어 있다면, 모듈
# import random  # random은 단일 파일(모듈)
# print(random.randint(1, 10))  # 1~10 사이의 랜덤 숫자 출력 # random.randint(1, 10) <- 이거는 모듈.함수 / 경로에 대한 부분 

# 라이브러리가 여러 모듈을 포함하는 폴더라면? → 패키지
# import numpy  # numpy는 여러 모듈을 포함하는 패키지
# print(numpy.array([1, 2, 3]))  # 배열 생성

# numpy/
#  ├── __init__.py  # 패키지 초기화 파일
#  ├── core.py
#  ├── linalg.py
#  ├── random.py

# import numpy  # numpy 패키지 전체 가져오기

# print(numpy.random.randint(1, 10))  # 패키지.모듈.함수 형태로 접근 

# 요약하면
# from 패키지, 모듈이 올 수 있고 -> from 패키지면 뒤에 모듈만 가능하고 / from 모듈이면 뒤에 함수,클래스,변수 가능 
# import가 어떤 형식이 오는지에 따라 접근 경로가 달라짐 
# 함수, 변수를 가져오면 바로 사용 가능하고 
# 모듈이 오면 경로로 함수, 변수를 접근해야되고
# 클래스가 오면 객체 생성해서 사용 

# # my_module.py (모듈)
# pi = 3.14159

# # 사용 코드
# from my_module import pi  
# print(pi)  # 3.14159

# 모듈 전체 가져온 후 변수사용

# import my_module  
# print(my_module.pi)  # 3.14159

# import 모듈 후 클래스 사용 

# # my_module.py (모듈)
# class Person:
#    def __init__(self, name):
#        self.name = name

#    def greet(self):
#        return f"안녕하세요, 저는 {self.name}입니다!"


# # main.py (사용 코드)
# import my_module  

# p = my_module.Person("윤수")  # 클래스 사용하려면 객체 생성
# print(p.greet())  # 출력: 안녕하세요, 저는 윤수입니다!

# 내장 함수는 Python에서 기본 제공하는 함수로 별도의 import 없이 사용 가능
# 표준 라이브러리는 Python이 기본 제공하는 모듈로, import 해서 사용 / 별도 설치 없이
# 외부 라이브러리는 다른 개발자가 만든 라이브러리로, pip install을 통해 설치해야 사용


