# ------------------------------------------------------------------
# Tuple 데이터 자료형 살펴보기
# - 내장함수 : len(), max(), min(), sum()
# - 연산자 : 덧셈, 곱셉, 멤버연산자 
# ------------------------------------------------------------------
nums = 11,22,33,44,55

## 내장함수 ---------------------------------------------------------
print(f'nums의 개수 : {len(nums)}개')
print(f'nums의 최대값 : {max(nums)}')
print(f'nums의 최소값 : {min(nums)}')
print(f'nums의 합계 : {sum(nums)}')
print(f'nums의 정렬 : {sorted(nums)},{sorted(nums,reverse=True)}')

print( max('abc','abC') )
print( sorted(('abc','Zoo')) )
# print( sum('sum','Zoo') ) 에러발생 정수만 가능 111,22 가능

## 연산자 ----------------------------------------------------------
## 덧셈
data1 = 11,22
data2 = 'A','B','C'

print(data1+data2)

## 곱셈 : tuple*int
print(data1*3)

## 곱셈 : tuple*int
print(data1*3)

## 멤버연산자 => in, not in
print(11 in data1)
print('A' in data1)