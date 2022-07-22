# 문자열
sentence = 'hello, world'
print(sentence)
sentence2 = "hello, world"
print(sentence2)
sentence3 = """
hello
,
world
"""
print(sentence3)

# 슬라이싱
jumin = "991122-2111111"

# index 0부터 시작
print("성별 : " + jumin[7]) # index 7번쩨 글자
print("연 : " + jumin[0:2]) # index 0부터 2 전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6 전까지
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤에서부터 : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())  # python 배열의 첫 번째 글자가 대문자인지 확인하고 boolean 리턴
print(len(python))
print(python.replace("Python", "Java")) # 찾을 문자, 바꿀 문자

index = python.index("n")
print(index)

index = python.index("n", index + 1) # 찾을 문자, 시작 위치(5+1)
print(index)

print(python.find("n"))
print(python.find("Java")) # 찾을 문자가 없을 경우 -1 반환
# print(python.index("Java")) # error

print(python.count("n")) # 찾는 문자열이 몇 번 반복되는지

# 문자열 포맷
# print("a" + "b")
# print("a", "b")

# 방법 1
print("나는 %d살입니다." %20) # %d : 정수
print("나는 %s를 좋아해요." %"파이썬") # %s : 문자열
print("Apple은 %c로 시작해요." %"A") # %c : 캐릭터(1글자)
print("나는 %s색과 %s색을 좋아해요."  %("파란","빨간"))

# 방법2
print("나는 {}살입니다.".format(20))
print("나는 {1}색과 {0}색을 좋아해요.".format("빨간","파란"))

# 방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))

# 방법4 (v3.6 이상)
age = 10
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출문자
print("Red Apple\rPine") # 커서를 맨 앞으로 이동
print("Redd\bApple")

# 퀴즈
# 1. http:// 제외
URL = "http://naver.com"

# print(URL[7:])
# URL = URL[7:]
# => http:// 가 어느 부분에서 나올지 알 수 없기 때문에 문자열을 끊으면 안 되고, replace() 함수를 써야 한다.
URL = URL.replace("http://","")

# 2. 처음 만나는 점 이후 부분 제외
# print(URL[:URL.find(".")])
URL = URL[:URL.find(".")]

# 3. 남은 글자 중 처음 세 자리 + 글자 개수 + 글자 내 'e' 개수 + "!"
PW = URL[:3]+str(len(URL))+str(URL.count("e"))+"!"

# 출력

