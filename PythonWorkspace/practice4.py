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