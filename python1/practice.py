print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*7)
print(5 > 10 )
print(5 < 10 )
print(True )
print(False )
print(not True)
print(not False)
print(not (5 > 10))

# 주석 
#ctrl + / #
# ㅇㅇ
# ㅋㅋ
# ㅎㅎ
'''이렇게 하면 여러문장이 주석처리가 됩니다'''

# 변수
name ="푸바오"
print(name+" 잘 지내니")

#사칙연산 
print(1+1) #2
print(3-2) #1
print(5*2) #10
print(6/3) #2

print(2**3) #2^3 = 8
print(5%3) # 나머지 구하기 2 
print(10%3) #1 
print(5//3) #1
print(10//3) #3 

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3==3) #True
print(4 == 2) #False
print(3 + 4 == 7) # True

print(1 !=3) #True
print(not(1 !=3)) #False

print((3 > 0) and (3 < 5)) # True
print((3 > 0 ) & (3 < 5) ) # True

print( (3 > 0) or ( 3 > 5)) # True 
print((3 > 0) | (3> 5)) # True

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False

print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20 
number = 2 + 3 * 4 # 14 
print(number)
number = number + 2 # 16 
print(number)
number +=2 #18
print(number)
number *=2 # 36
print(number)
number /=2 # 18 
print(number)
number -= 2 #16 
print(number)
number %=2  # 0 
print(number)

number %= 5 #1 
print(number)
print(abs(-5)) #5
print(pow(4, 2)) # 4^2 = 4*4 = 16 
print(max(5, 12)) # 12
print(min(5, 12)) # 5 
print(round(3.14)) # 3 
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 내림. 4
print(ceil(3.14)) # 올림. 4
print(sqrt(16)) # 제곱근 4 

from random import * 
print(random()) #0.0~1.0미만의 임의의 값 생성 
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10 )) # 0 ~ 10 미만의 임의의 값 생성 
print(int(random() * 10 ) + 1) # 1~ 10 이하의 임의의 값 생성 

print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성 
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성 
print(randint(1, 45)) # 1~ 45 이하의 임의의 값 생성 

date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다. ")

sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """나는 소년이고, 
파이썬은 쉬워요"""
print(sentence3)

jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 ~ 2 직전까지 (0, 1) 
print("월 : " + jumin[2:4]) # 01
print("일 : " + jumin[4:6]) # 01
print("생년월일 : " + jumin[:6]) #990120 처음부터 6 직전까지 
print("뒤 7자리 : " + jumin[7:]) #1234567 7부터 끝까지 
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지 

python = "Python is Amazing"
print(python.lower()) 
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("java"))
#print(python.index("Java"))
print("hi")
print(python.count("n"))

#문자열 포맷
print("a" + "B")
print("a", "bb")

print("난 %d 살입니다." % 20)
print("난 %s 을 좋아해요." % "파이썬")
print("Apple %c 로 시작해요" % "A")

# %s
print("나는 %s 살입니다." % 20)
print("나는 %s 색과 %s 색을 좋아해요. " % ("파란", "빨간"))

print("나는 {} 살입니다.".format(20))
print("나는 {1} 색과 {0} 색을 좋아해요.".format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))

# 파이썬 3.6 이상 
age = 20 
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출문자
print("백문이 불여일견 \n백견이 불여일타")

print("나는 \"푸바오\"입니다.")

# \\ : 문장내에서 \
print("I:\\Downloads")

# \r : 커서를 맨 앞으로 이동 
print("Red Apple\rPine")

#\b : 백스페이스(한 글자 삭제)
print("Redd\bApple")

#\t : 탭
print("Red\tApple")

url = "http://naver.com"
my_str = url.replace("http://","") 
my_str = my_str[:my_str.index(".")]
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다. ".format(url, password))

