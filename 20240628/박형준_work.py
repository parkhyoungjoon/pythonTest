# 챕터 10 연습문제 : range로 리스트만들기
a = list(range(5, -10, -2))
print(a)

# 챕터 10 심사문제 : range로 튜플만들기
num = input()
result = tuple(range(-10,10,int(num)))
print(result)

# 챕터 11 연습문제 : 최근 3년간 인구 출력하기
year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
pupulation = [1024679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]
print(year[-3:])
print(pupulation[-3:])

# 챕터 11 연습문제 : 인덱스가 홀수인 요소 출력하기
n= -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
print(n[1::2])

# 챕터 11 심사문제 : 리스트의 마지막 부분 삭제하기
texts = input().split()
del (texts[-5:])
print(texts)

# 챕터 11 심사문제 : 문자열에서 인덱스가 홀수인 문자와 짝수인 문자 연결하기
txt1 = input()
txt2 = input()
str1 = str(txt1[1::2])
str2 = str(txt2[::2])
print(str1,str2,sep='')