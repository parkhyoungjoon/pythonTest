# 01
print('Hello World')

# 02
print('Mary\'s cosmetics')

# 03
print('신씨가 소리질렀다 "도둑이야!"')

# 04
print('C:\\Windows')

# 05
print("안녕하세요.\n만나서\t\t반갑습니다.") #\n : 줄바꿈 \t : 탭간격

# 06
print("오늘은", "일요일") # 오늘은 일요일

# 07
print('naver','kakao','sk','samsung', sep=';')

# 08
print('naver','kakao','sk','samsung', sep='/')

# 09
print("first",end='');print("second")

# 10
print(5/3)

# 11
삼성전자 = 50000
삼전금액 = 50000*10
print(삼전금액)

# 12
시가총액 = '298조'
현재가 = '50000원'
PERs = 15.79

# 13
s = "hello"
t = "python"

print(f'{s}! {t}')

# 14
num = 2 + 2 * 3 # 8 

# 15
a = "132"
print(type(a))

# 16
num_str = "720"
num_str = int(num_str)
print(num_str)

# 17
num = 100
num = str(100)
print(num)

# 18
str1 = '15.79'
str1 = float(str1)
print(str1)

# 19
year = "2020"
year = int(year)
years = range(year-2,year+1)
print(years[0],years[1],years[2])

# 20
airprice = 48584
months = 36
price = airprice * months
print(price)

# 21
letters = 'python'
print(letters[0],letters[2])

# 22
license_plate = "24가 2210"
print(license_plate[-4:])

# 23
string = "홀짝홀짝홀짝"
print(string[::2])

# 24
string = "PYTHON"
print(string[::-1])

# 25
phone_number = "010-1111-2222"
print(phone_number[0:3],phone_number[4:8],phone_number[9:])

# 26
print(phone_number[0:3],phone_number[4:8],phone_number[9:], sep = '')

# 27
url = "http://sharebook.kr"
domain = url.split('.')
print(domain[1])

#28
# lang = 'python' 에러발생 원소값 변경불가
# lang[0] = 'P'
# print(lang)

# 29
string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)

# 30
string = 'abcd'
string.replace('b', 'B')
print(string) # abcd 그대로 출력 문자열 구문들은 값을 반환하지만 저장하지는 않기 때문

# 31
a = "3"
b = "4"
print(a + b) # "34"

# 32
print("Hi" * 3) # "HIHIHI"

# 33
print('-'*80)

# 34
t1 = 'python'
t2 = 'java'
print((t1 + ' ' + t2 + ' ')*4)

# 35
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print('이름 : %s 나이 : %d \n이름 : %s 나이 : %d'%(name1,age1,name2,age2))

# 36
print('이름 : {} 나이 : {} \n이름 : {} 나이 : {}'.format(name1,age1,name2,age2))

# 37
print(f'이름 : {name1} 나이 : {age1} \n이름 : {name2} 나이 : {age2}')

# 38
상장주식수 = "5,969,782,550"
txts = 상장주식수.replace(',','')
num = int(txts)
print(num,type(num))

# 39
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 40
data = "   삼성전자    "
data = data.strip()
print(data)

# 41
ticker = "btc_krw"
ticker = ticker.upper()
print(ticker)

# 42
ticker = "BTC_KRW"
ticker = ticker.lower()
print(ticker)

# 43
ticker = "Hello"
ticker = ticker.capitalize()
print(ticker)

# 44
file_name = "보고서.xlsx"
file_name.endswith('xlsx')
print(file_name)

# 45
file_name = "보고서.xlsx"
file_name.endswith(('xlsx','xls'))
print(file_name)

# 46
file_name = "2020_보고서.xlsx"
file_name.startswith('xlsx')
print(file_name)

# 47
a = "hello world"
a = a.split()
print(a)

# 48
ticker = "btc_krw"
ticker = ticker.split('_')
print(ticker)

# 49
date = "2020-05-01"
date = date.split('-')

# 50
data = "039490     "
data.rsplit()
print(data)

# 51
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
print(movie_rank)

# 52
movie_rank.append('배트맨')
print(movie_rank)

# 53
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1,'수퍼맨')
print(movie_rank)

# 54
del movie_rank[3]
print(movie_rank)

# 55
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2:]
print(movie_rank)

# 56
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
lang3 = lang1 + lang2
print(lang3)

# 57
nums = [1, 2, 3, 4, 5, 6, 7]
print(f'max : {max(nums)}\nmin : {min(nums)}')

# 58
nums = [1, 2, 3, 4, 5]
print(sum(nums))

# 59
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 60
nums = [1, 2, 3, 4, 5]
avg = sum(nums) / len(nums)
print(avg)

# 61
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 62
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# 63
print(nums[1::2])

# 64
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

#65
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[::2])

#66
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

#67
print("/".join(interest))

#68
print("\n".join(interest))

#69
string = "삼성전자/LG전자/Naver"
interest = string.split('/')
print(interest)

#70
data = [2, 4, 3, 1, 5, 10, 9]
data = sorted(data)
print(data)

#71
my_variable = ()
print(my_variable, type(my_variable))

#72
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
print(movie_rank)

# 73
num = (1)
print(num,type(num)) # 반복되지 않는 인수 단일 int이기에 튜플이 아닌 인트로 정의

# 74
# t = (1, 2, 3)
# t[0] = 'a' 튜플은 요소/원소 값을 변경, 삭제 할 수 없음 읽기전용 시퀀스

# 75
t = 1, 2, 3, 4 # ()가 생략되어도 튜플로 저장됨
print(t,type(t))

# 76
t = ('A', 'B', 'C') # t = ('a', 'b', 'c') 튜플의 값은 수정되지 않기때문에 다시 정의해야 함

# 77
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(interest,type(interest))

# 78
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)
print(interest,type(interest))

# 79
temp = ('apple', 'banana', 'cake') 
a, b, c = temp # a = 'apple', b = 'banana', c = 'cake'
print(a, b, c) # 'apple', 'banana', 'cake' 출력됨

# 80
nums = range(2,99,2)
nums = tuple(nums)
print(nums, type(nums))