import math

array = []
K = int(input()) # 35
yes = 0

while(1):
    yes = int(math.log2(K))
    array.append(yes)
    K = yes 
    if yes == 0:
        break

# print(array)

index = (array[0] + 1) - array[1]- 1 

firstNumber = "4" * (array[0]+1)
secondNumber = firstNumber[:index] + "7" + firstNumber[index+1:]
print(int(secondNumber))


# 5 2 1 0

# 5 -> 6자리부터 시작 # K - (2^5-2) = 5  // log2(5) = 2 // 5 - 2 ^ 2 // 1 // log2(1) = 0 이 될 때까지 


# 444444
# 444447
# 444474
# 444477  

# 444744

# 444444

# 2째자리까지 변화 

# 444744 # 3째자리부터 

# 6 # (2^6-2)

# 2 + 4 + 8 + 16 = 30 # 2^5 -2 (초기 1이 없으므로)

