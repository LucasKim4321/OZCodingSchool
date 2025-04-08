from multiprocessing import Process, Value

# multiprocessing.Value 프로세스간에 값을 공유할 때 사용

def counter1(snum, cnt):
    for i in range(cnt):
        snum.value += 1

def counter2(snum, cnt):
    for i in range(cnt):
        snum.value -= 1

if __name__ == "__main__":
    shared_number = Value('i', 0)  # i = 0
    p1 = Process(target=counter1, args=(shared_number, 5000))
    p1.start()

    p2 = Process(target=counter2, args=(shared_number, 5000))
    p2.start()

    p1.join()
    p2.join()

    print("finally, number is", shared_number.value)

# 공유 값을 불러올 때 제한이 없어서
# 값을 불러오는 시점이 달라져 결과 값이 매번 달라짐

# Process.join()은 다음과 같은 역할을 합니다:
# 해당 프로세스가 종료될 때까지 메인 프로세스(현재 실행 중인 코드)를 일시 중지시킨다.