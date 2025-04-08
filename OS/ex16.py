import threading
from multiprocessing import Process, Value, Lock

# multiprocessing.Value 프로세스간에 값을 공유할 때 사용

# 스레드에서도 똑같이 테스트

# 락을 걸지 않을 경우
# def counter1(snum, cnt):
#     try:
#         for i in range(cnt):
#             snum.value += 1
#     finally:
#         print("counter1 done")

# def counter2(snum, cnt):
#     try:
#         for i in range(cnt):
#             snum.value -= 1
#     finally:
#         print("counter2 done")

# if __name__ == "__main__":
#     shared_number = Value('i', 0)  # i = 0

#     t1 = threading.Thread(target=counter1, args=(shared_number, 10000))
#     t1.start()

#     t2 = threading.Thread(target=counter2, args=(shared_number, 10000))
#     t2.start()

#     t1.join()
#     t2.join()

#     print("finally, number is", shared_number.value)

# 락을 걸 경우
def counter1(snum, cnt, lock):
    lock.acquire()
    try:
        for i in range(cnt):
            snum.value += 1
    finally:
        lock.release()

def counter2(snum, cnt, lock):
    lock.acquire()
    try:
        for i in range(cnt):
            snum.value -= 1
    finally:
        lock.release()


if __name__ == "__main__":
    lock = Lock()
    shared_number = Value('i', 0)  # i = 0

    t1 = threading.Thread(target=counter1, args=(shared_number, 10000, lock))
    t1.start()

    t2 = threading.Thread(target=counter2, args=(shared_number, 10000, lock))
    t2.start()

    t1.join()
    t2.join()

    print("finally, number is", shared_number.value)

# lock을 통해 연산이 완전히 끝난 후 값을 가져오기 때문에 정확한 계산이 가능함.

# Process.join()은 다음과 같은 역할을 합니다:
# 해당 프로세스가 종료될 때까지 메인 프로세스(현재 실행 중인 코드)를 일시 중지시킨다.
