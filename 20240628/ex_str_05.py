# ------------------------------------------------------------------
# 문자열 str 데이터 다루기
#  - 이스케이프문자 : 특수한 의미를 가지는 문자
#       * 형식 : \문자1개
#       * '\n' - 줄바꿈 문자
#       * '\t' - 탭간격 문자
#       * '\'' - 작은따옴표 문자
#       * '\"' - 큰따옴표 문자
#       * '\\' - 역슬래시 문자, 경로(path), URL 관련
#       * '\U' - 유니코드
#       * '\a' - 알람소리 문자
# ------------------------------------------------------------------
msg = "오늘은 좋은날\n내일은 주말이라 행복해요"
print(msg)

msg = '오늘은 나의\'생일\'이야'
print(msg)

file = 'C:\\Users\\KDP-38\\Documents\\mongoDB\\Data'
print(file)

file = r'C:\Users\KDP-38\Documents\mongoDB\Data'
print(file)

msg = "Happy\tNew\tYear"
msg2 = r"Happy\tNew\tYear"
print(msg,msg2)