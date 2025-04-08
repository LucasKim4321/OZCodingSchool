from multiprocessing import Process
# 멀티 프로세싱 프로그래밍할 때 사용

import os
import time

def coke():
    while True:
        try:
            print("콜라 프로세스 아이디 : ", os.getpid())
            print("부모 프로세스 아이디 : ", os.getppid())
            print("--------------------------------")
        except KeyboardInterrupt:
            break

def cider():
    while True:
        try:
            print("사이다 프로세스 아이디 : ", os.getpid())
            print("부모 프로세스 아이디 : ", os.getppid())
            print("--------------------------------")
        except KeyboardInterrupt:
            break

def juice():
    while True:
        try:
            print("주스 프로세스 아이디 : ", os.getpid())
            print("부모 프로세스 아이디 : ", os.getppid())
            print("--------------------------------")
        except KeyboardInterrupt:
            break


# main 프로세스의 동작을 조건문으로 정의
if __name__ == '__main__':
    print('07.py 프로세스 아이디 :', os.getpid())  # 05.py의 id가 나옴
    print("--------------------------------")

    child1 = Process(target=coke)  # 하위 프로세스를 만듬
    child1.start()
    time.sleep(0.5)

    child2 = Process(target=cider)
    child2.start()
    time.sleep(0.5)

    child3 = Process(target=juice)
    child3.start()
    time.sleep(0.5)

# 맥에서 현재 실행중인 프로세스를 보는 명령어
# ps
# ps -el | grep python