# 인터럽트 예제

import time    # 시간 제어
import signal  # 신호 처리

def handler(signum, frame):  # signum: 인터럽트 유형 번호 frame: 스텍영역 정보 출력
    print('키보드 인터럽트 감지')
    print('신호 번호:', signum)
    print('스택 프레임:', frame)
    exit()  # 무한루프가 발생하면 대응

# signal.SIGINT: 키보드 인터럽트 상수
signal.signal(signal.SIGINT, handler)

while True:
    print('2초 간격으로 출력 중...')
    time.sleep(2)
