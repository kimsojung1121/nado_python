cabinet = {3:"유재석", 100:"김태호"}

# 출력 방법 1
print(cabinet[3])
print(cabinet[100])
# print(cabinet[5]) # 에러 발생

# 출력 방법 2
print(cabinet.get(3))
print(cabinet.get(5)) # 에러 x
# 값이 존재하지 않을 경우 default 값 설정
print(cabinet.get(5, "값이 없습니다."))

# 값이 존재하는지 확인 - boolean 리턴
print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}

cabinet["A-3"] = "김종국" #변경
cabinet["C-20"] = "조세호" #추가
print(cabinet)

del cabinet["A-3"]
print(cabinet)

# key만 출력
print(cabinet.keys())

# values 출력
print(cabinet.values())

# 쌍으로 출력
print(cabinet.items())

# 모두 삭제
cabinet.clear()
print(cabinet)