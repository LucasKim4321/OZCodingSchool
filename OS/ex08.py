# 내 파이썬 프로그램의 이름을 알아보자.

import psutil

# iteration 반복
# process_iter() 전체 프로세스에 반복적으로 접근하는 함수
for proc in psutil.process_iter():
    try:
        ps_name = proc.name()

        # 크롬 하나만 열어도 여러개의 하위 프로세서가 돌아간다.
        # if "Python" in ps_name:
        # if "python" in ps_name:
        if "ex08.py" in ps_name:
            child = proc.children()

            print(ps_name, proc.status(), proc.parent(), child)

            if child:
                print(f'{ps_name}의 자식 프로세스', child)

    except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # 프로세스가 이미 종료되었거나 접근 권한이 없을 경우 무시
        continue
