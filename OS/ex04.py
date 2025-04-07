import psutil

# iteration 반복
# process_iter() 전체 프로세스에 반복적으로 접근하는 함수
for proc in psutil.process_iter():
    try:
        ps_name = proc.name()

        # 크롬 하나만 열어도 여러개의 하위 프로세서가 돌아간다.
        if "Chrome" in ps_name:
            child = proc.children()

            print(ps_name, proc.status(), proc.parent(), child)

            if child:
                print(f'{ps_name}의 자식 프로세스', child)

    except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # 프로세스가 이미 종료되었거나 접근 권한이 없을 경우 무시
        continue


# Google Chrome Helper (Renderer) running psutil.Process(pid=828, name='Google Chrome', status='running', started='09:51:50') []

# 이름, 상태, 부모프로세스, 자식프로세스

# 이름 : Google Chrome Helper (Renderer)
# 상태 : running 실행중임을 의미
# 부모 프로세스 : psutil.Pross(...)
# 자식 프로세스 : [] 리스트안의 프로세스

# 리스트안에 뭔가 있으면 자식 프로세스를 가진 부모 프로세스