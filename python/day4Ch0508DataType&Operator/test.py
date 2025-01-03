#py -> python의 약자
#test 라는 이름을 가진 파일은 python
#.py 파일의 성격을 나타냅니다.
#.py는 확장자라고도 한다.

#주석이 많으면 느려지기도 함. 필요한 메모만. 공부할 땐 하고싶은 만큼 하기

"""
자료와 처리
프로그래밍은 자료와 처리 두가지로 표현할 수 있습니다.
지금도 우리 주변에서는 자연스럽게 자료가 생성되고 처리되고 있습니다.

(예시)
- 수강생들이 제출하는 과제는 '자료'이고, 제출 여부를 확인하는 과정을 '처리'라고 할 수 있습니다.
- 생일인 친구에게 보내는 축하 메시지는 '자료'이고, 이를 전송 또는 전달하는 행위는 '처리'라고 할 수 있습니다.

처리되는 부분을 프로그래밍 언어로 구현해서 처리하는 걸 앞으로 여러분들이 하게 되실 공부 또는 업무라고 생각합니다.
"""

"""
자료형(자료)
String(문자형) : "방가워요 여러분" ,"ㅇ", "1" "82취직하고 싶다면 오즈코딩스쿨"
"로 시작해서 "로 끝나는 걸 문자형으로 인식.  ''도 가능
Number(숫자형) : 1, 2, 3.2, 35, 123213123
                -> 파이썬의 최대 단점 메모리 누수가 심하다. 자바의 경우 상세하게 지정.
                -> 파이썬의 경우 지정된 메모리 공간이 부족하면 배로 늘려서 사용
Boolean(불) : 참과 거짓 -> True, False
"""

# New-Item test.py -Type File
# python3 test.py

print(3, end="")
print(5, end="바보")
print(6, 4, 5, 6, sep="")

# end: str | None = "\n" 한줄띄는것 : 개행,    \t, \n : 제어문자, 이스케이프 시퀀스

print('3\n6\n9')

print('010', 2234, 4566) #010 0000 0000

print('010', 2234, 4566, sep="-") #010-0000-0000
# 숫자형 중에서 문자형태로 바꿀 수 있는것들은 문자와 결합할 때 자동적으로 문자형으로 바꿔서 진행한다.

print(int(2.2), str(2.2))

phone_num = "010-1234-5678"
#phone_num 문자형의 성격을 갖습니다.
#1
num = phone_num.split("-")
phone_num = num[0]+num[1]+num[2]
print("case1:",phone_num)

#2
phone_num = "010-1234-5678"
phone_num = ''.join(phone_num.split("-"))
print("case2:",phone_num)

#3
phone_num = "010-1234-5678"
print("case3:",phone_num.replace("-",""))

"""
이름 의미한다.

password = 1234 # '=' 대입한다. 할당한다.

name = '태진'

print(name)
"""

name = '태진'
print(name)

name = '오즈코딩' #재할당
print(name)

#변수 선언시 javascript 처럼 var let const와 같은 구분이 없음.

num_1 = 1
num_2 = 2

print(1+2)
print(num_1 + num_2)

str_1 = "안녕하세요"
str_2 = " 여러분"

print(str_1 + str_2)

print("{}".format(10))  # [] : 대괄호  /  {} : 중괄호  /  () : 소괄호

print("열심히 하는 {}기 {}입니다.".format(9, "백엔드"))


# f-string
num = 6
position = "백엔드"

print(f"열심히 하는 {num}기 {position}입니다.")
print(f"열심히 하는 {num}기 '{position}'입니다.")
print(f'열심히 하는 {num}기 "{position}"입니다.')

"""

사칙연산
+, -, *, /, //, %

/ : 나누기(실수로 나옴)
// : 나누기(정수 부분만 나옴)
% : 나눈 나머지 표시(정수)
**2 : 제곱
**3 : 세제곱
**0.5 : 제곱근


연산자 우선순위
1순위 : ()
2순위 : **
3순위 : * / // %
4순위 : + -


"""

position = "백엔드"
get_in = " 3명 타세요"

print(position * 10)
print(position + get_in)
print(position + get_in * 3)
print((position + get_in) * 3)