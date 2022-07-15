# <애완동물을 소개해 주세요~>
# 동일하게 반복되는 객체를 변수로 선언
# 코드 변경에 용이하다.
animal = "고양이"
name = "시루"
age = 4
hobby = "산책"
is_adult = age >= 3

# 변수 선언 이전 코드
# print("우리집 고양이 이름은 시루예요")
# print("시루는 곧 4살이며,  장난감을 좋아해요")
# print("시루는 어른일까요? True")

#변수 선언 이후 코드
print("우리집" + animal + " 이름은 " + name + "예요")
hobby = "낮잠"
# print(name + "는 곧 " + str(age) + "살이며,  " + hobby + "을 좋아해요")
print(name , "는 곧" , age , "살이며, " , hobby , "을 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))


# 퀴즈
# station = "사당"
# station = "신도림"
station = "인천공항"
print(station , "행 열차가 들어오고 있습니다.")
