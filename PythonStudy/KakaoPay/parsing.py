def convert_string(s):
    num_dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
                'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    
    print(num_dict.items())
    for key,value in num_dict.items():
        s = s.replace(key,value)
    return int(s)

s = "one4seveneight"
print(convert_string(s))  


# 영어로 된 숫자 -> 해당하는 아라비아 숫자로 변환

# AttributeError
# 파이썬에서 객체가 갖고 있지 않은 속성(attribute)이나 메서드를 
# 호출하려고 시도했을 때 발생하는 오류
# 특정 객체가 지원하지 않는 속성이나 메서드에 접근하려고 할 때 파이썬은 AttributeError를 발생시켜 문제가 있음을 알림

# "has no attribute 'item'"이라는 표현은 파이썬이 지정된 객체(dict object 즉, 사전 객체)에서 
# item이라는 이름의 속성이나 메서드를 찾을 수 없다는 것

# replace() 메서드
# str.replace(old, new, count)
# 