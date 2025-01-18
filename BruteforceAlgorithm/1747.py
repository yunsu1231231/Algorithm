import math

N = int(input())

def prime(n):
    if n<=1:
        return False
    if n == 2: 
        return True 
    if n % 2 == 0: 
        return False
    
    for i in range(3,int(math.sqrt(n)) +1,2):
        if n % i == 0:
            return False
        
    return True 
    
def palindrome(n):
    s = str(n)
    
    return s == s[::-1]

while(1):
    if prime(N) and palindrome(N):
        print(N)
        break 
    else:
        N += 1 
        
# n이 어떤 수로 나누어지는지 확인할 때, 그 수가 √n을 초과할 필요가 없다 



# Pylance는 **Visual Studio Code (VS Code)**에서 사용되는 Python 언어 서버

# reportUndefinedVariable은 Pylance 또는 Pyright에서 제공하는 설정 중 하나입니다. 
# 이 설정은 코드에서 정의되지 않은 변수를 사용했을 때, 해당 변수를 undefined variable로 간주하고 경고를 발생시킬지 여부를 결정

# Traceback = 예외가 발생한 위치와 호출 스택

# 파이썬에서 하나의 파일은 기본적으로 하나의 모듈
# in <module>은 파이썬의 모듈에서 코드가 실행된 부분

# NameError는 파이썬에서 정의되지 않은 변수나 이름을 사용할 때 발생하는 예외

# NameError와 같은 에러 이름들은 파이썬의 내장 예외 클래스
# 파이썬은 다양한 종류의 오류를 처리할 수 있도록 **예외(Exception)**를 정의

# 네, 맞습니다! 파이썬에서 발생한 예외는 콘솔에 예외 클래스의 이름과 함께 오류 메시지를 표시해주며, 
# 이 이름을 통해 어떤 종류의 오류가 발생했는지 알 수 있습니다.

# NameError: name 'x' is not defined
# NameError는 발생한 예외의 클래스 이름
# 뒤에 이어지는 부분은 오류의 세부 메시지로, 이 오류가 왜 발생했는지를 설명해줍니다.

# 파이썬에서는 함수 정의 순서가 중요합니다. 
# 코드에서 함수를 호출하려면 먼저 함수가 정의되어 있어야 합니다. 따라서 prime(N)을 호출하기 전에 prime 함수가 정의되어 있어야 합니다.

# TypeError는 파이썬에서 자료형이 맞지 않을 때 발생하는 예
# non-string은 문자열이 아닌 자료형을 의미

# explicit base는 명시적으로 지정된 진법

# explicit는 명시적인, 분명히 지정된이라는 뜻입니다. 
# 따라서 explicit base는 진법을 명시적으로 지정하는 것 
# int("101", 2)  # "101"을 2진수로 해석하여 10진수로 변환 -> 5

# 파이썬의 int() 함수는 문자열을 정수로 변환할 때 사용
# 기본적인 정수 변환: int("123")처럼 문자열을 정수로 변환하는 경우
# 진법을 명시적으로 지정하여 변환: int("101", 2)처럼 문자열을 특정 진법(예: 2진수, 8진수, 16진수 등)으로 변환하는 경우.
