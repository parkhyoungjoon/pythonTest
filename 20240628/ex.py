# -----------------------------------------------------------------------------------------
# 내장함수 map(함수명, 여러개데이터)
# -----------------------------------------------------------------------------------------
data = input('숫자 데이터 입력 : ')
print(type(data))

# 1개 문자열 ==> 여러개 문자열 분리
# 예) '10, 20, 30' ==> '10', '20', '30'
nums = data.split()

# 문자열 숫자 ==> 정수로 변환
result = map(int,nums)
print(type(result))

myfunc = int
result2 = map(myfunc, nums)
print(id(int), id(myfunc))

# -----------------------------------------------------------------------------------------
# 형변환 => 
#  - 자동형변환 : 컴퓨터가 진행, 작은 것 ==> 큰 것
#  - 수동형변환 : 개발자가 진행, 큰 것 ==> 작은 것
# -----------------------------------------------------------------------------------------
a=10
b=3
print(a/b)