# p035 print 출력
print('hello, world!')
print('hello, python')

# p037 
print('Hello, world!')

# p049 3챕터 연습문제
print('Hello, world!')
print('Python Programming')

# p049 3챕터 심사문제
print('Hello, world!\nHello, world!')

# p050 ;실험
print('Hello'); print('1234')

# p051 한줄주석
# Hello, world!
print('Hello, world!')
# print('Hello, world!')
a = 1 + 2 # 더하기
print('Hello, world!') #printf('1234567890')

#블록주석
# print('Hello, world!')
# print('1234567890')

# 들여쓰기 에러 발생

# if a == 10:
# print('10입니다.')

# 올바른 방식
if a == 10:
    print('10입니다.')

# 코드블록
if a == 10:
    print('10')
    print('입니다.')

# 5챕터 연습문제: 아파트에서 소음이 가장 심한 층수 출력
print(int(0.2467*12+4.159))

# 5챕터 심사문제: 스킬공격력 출력하기
AP = 102
print(AP*0.6+225)

# p069 두숫자 합 구하기
a = input('첫 번째 숫자를 입력하세요: ')
b = input('두 번째 숫자를 입력하세요: ')
print(a+b)

# p070 두숫자 합 정수로 구하기
a = int(input('첫 번째 숫자를 입력하세요: '))
b = int(input('두 번째 숫자를 입력하세요: '))
print(a+b)

# p071 입력값을 변수 두 개에 저장하기
a, b = input('문자열 두 개를 입력하세요: ').split()
print(a)
print(b)

# p071 두 숫자 합 구하기
a, b = input('문자열 두 개를 입력하세요: ').split()
print(a+b)

# p072 두 숫자 합 정수로 구하기
a, b = input('문자열 두 개를 입력하세요: ').split()
a = int(a)
b = int(b)
print(a+b)

# p073 map을 통해 정수로 변환
a, b = map(input('문자열 두 개를 입력하세요: ').split())
print(a+b)

# 6챕터 연습문제
a, b, c = map(int, input().split)

# 6챕터 심사문제:변수만들기
a = 50
b = 100
c = 'None'

print(a)
print(b)
print(c)
# 6챕터 심사문제:평균 점수 구하기
class1, class2, class3, class4 = map(int, input().split())
average = (class1+class2+class3+class4)/4
print(average)

# p079 end사용하기
print(1)
print(2)
print(3)

print(1, end='')
print(2, end='')
print(3)

print(1, end=' ')
print(2, end=' ')
print(3)

# 7챕터 연습문제 날짜와 시간 출력하기
year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59
print(year, month, day, sep='/', end=' ')
print(hour, minute, second, seip=':')

# 7챕터 심사문제 날짜와 시간 출력하기
year, month, day, hour, minute, second = input().split()
print(year, month, day, sep='-')
print(hour, minute, second, sep=':')

# 8챕터 연습문제: 합격여부 출력하기
korean = 92
english = 47
mathematics = 86
science = 81
print(korean >= 50 and english >= 50 and mathematics >= 50 and science >= 50)

#8챕터 심사문제: 합격여부 출력하기
korean, english, mathematics, science = map(int,input().split())
answer = (korean >= 90 and english > 80 and mathematics > 85 and science >= 80)
print(answer)

# p97 문자열 안에 따옴표 넣기
single_quote1 = '''"안녕하세요." 
'파이썬'입니다.'''
double_quote1 = """"Hello." 
'Python'"""
double_quote2 = """"Hello." 'Python'"""

print(single_quote1)
print(double_quote1)
print(double_quote2)

# 챕터9 연습문제

s = '''Python is a programming language that lets you work quickly
and
intergrate systems more effectively'''
print(s)

# 챕터 9 심사문제: 여러줄로 된 문자열 사용하기
s = """'Python' is a "programming language"
that lets you work quickly
and
intergrate systems more effectively.
"""
print(s)