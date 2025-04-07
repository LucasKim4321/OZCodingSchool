
# pip3 install psutil
# 프로세스에 대한 주요 기능을 추가로 구현할 수 있다.

# 내 컴퓨터에서 돌아가는 프로세스 조회하기

import psutil

# iteration 반복
# process_iter() 전체 프로세스에 반복적으로 접근하는 함수
for proc in psutil.process_iter():
    try:
        ps_name = proc.name()

        # print(ps_name) # 이렇게 하면 실행중인 프로세스 전부 보여줌
        # 이미 종료되었거나 접근 권한이 없는 경우 발생하는 예외가 발생해서 예외 처리함

        if "chrome" in ps_name:
        # if "Chrome" in ps_name:
            print(ps_name, proc.pid) # 프로세스 이름이 크롬인 것의 이름과 pid를 출력

    except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # 프로세스가 이미 종료되었거나 접근 권한이 없을 경우 무시
        continue
