# 연산자
print(1+1)
print(3-1)
print(5*2)
print(6/3)

print(2**3) # 2^3
print(5%3) # 나머지
print(10//3) # 몫

print(10 > 3)
print(4 >= 7)
print(10 < 3)
print(5 <= 5)

print(3==3)
print(3 + 4 == 7)
print(3 != 2)
print(not(1 != 3))

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

print((3 > 0) or (3 < 5))
print((3 > 0) | (3 < 5))

print(5 > 4 > 3)

number = 2
number *= 3
print(number)

number /= 2
print(number)

# 숫자 처리 함수
print(abs(-5))
print(pow(4,2))
print(max(2, 10))
print(min(2, 10))
print(round(3.14)) # 3
print(round(3.9))  # 4

from math import *

print(floor(4.9)) # 4
print(ceil(4.1))  # 5
print(sqrt(16))   # 4

# 랜덤 함수
from random import *

print(random())   # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성(정수)
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

print(int(random() * 45) + 1)  # 1 ~ 45 이하의 임의의 값 생성

print(randrange(1, 46))
print(randint(1, 45))

# 퀴즈
from random import * # 렌담 라이브러리 import

# 1)
day = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월", day, "일로 선정되었습니다.")

# 2)
day = randrange(4, 29)
print("오프라인 스터디 모임 날짜는 매월", day, "일로 선정되었습니다.")

# 3)
day = int(random() * 24 ) + 4 # 0 ~ 24 미만 =>(3일 더하기) 4 ~ 28 이하 
print("오프라인 스터디 모임 날짜는 매월", day, "일로 선정되었습니다.")
