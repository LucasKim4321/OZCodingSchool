import threading
import os
import time

def something(word):

    while True:
        print(word)
        time.sleep(3)

if __name__ == "__main__":
    print('기존 푸로세스 아이디 : ', os.getpid())
    t = threading.Thread(target=something, args=('happy',))
    t.daemon = True  # 데몬 스레드 설정 : 메인 기능이 끝나면 같이 끝나게 설정
    t.start()
    print('메인 스레드에서 반복문 시작')

    while True:

        try:
            print('daliy...')
            time.sleep(1)

        except KeyboardInterrupt:
            print('good bye~')
            break

# 메인 스레드
# 파이썬 프로세스가 생성이 되면 기본적으로 메인 스레드가 내부에 생김
# 메인 문에서 돌아가는 기능은 메인 스레드에서 실행됨.
# 현재 실습은 하나의 프로세스에서 2개의 스레드 가지는 상태