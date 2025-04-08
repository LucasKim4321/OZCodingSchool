from multiprocessing import Process, Pipe
import os

def send(conn):
    print(f'{os.getpid()}가 {os.getppid()}에게 데이터를 보낸다.')
    conn.send("Hello parent!")
    conn.close()

if __name__ == "__main__":
    parent, child = Pipe() # Pipe() 생성자 함수
    p = Process(target=send, args=(child,))
    p.start()
    print('기존 프로세스 아이디 : ', os.getpid())
    print(parent.recv())  # recv() : receive 자식 프로세스가 보낸 데이터를 받음. send()가 보낸 데이터를 받음.
    p.join()