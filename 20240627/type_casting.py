# -----------------------------------------------------------------
# 형변환 / 타입캐스팅
# - 자료형을 다른 종류의 자료형으로 변경
# - 종류
# * 자동/묵시적 형변환 : 컴퓨터
# * 수동/명시적 형변환 : 개발자 
# -----------------------------------------------------------------
age = 20.7

# float ---> int 변환
print(age,int(age))

age = int(age)
print(age, type(age))

# int ---> float 변환
age = float(age)
print(age, type(age))

# float --- str 변환
age = str(age)
print(age, type(age))