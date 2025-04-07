from multiprocessing import Process
# 멀티 프로세싱 프로그래밍할 때 사용

import os

def func():
    print('안녕, 나는 실험용으로 대충 만들어 본 함수야!')
    print('나의 프로세스 아이디 : ', os.getpid())
    print('나의 부모 프로세스 아이디 : ', os.getppid())  # ppid (parent process id)

# main 프로세스의 동작을 조건문으로 정의
if __name__ == '__main__':
    print('05.py 프로세스 아이디 :', os.getpid())  # 05.py의 id가 나옴
    child = Process(target=func).start()  # 하위 프로세스를 만듬