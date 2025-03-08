# from itertools import permutations

# # 입력 받기
# N, M = map(int, input().split())

# # 1부터 N까지의 숫자로 이루어진 순열 생성
# for seq in permutations(range(1, N + 1), M):
#     print(*seq)




N, M = map(int, input().split())

visited = [False] * (N + 1)  # 방문 여부 체크
result = []  # 현재 수열 저장

def backtrack():
    if len(result) == M:  # M개의 숫자를 모두 선택했으면 출력
        print(*result)
        return

    for i in range(1, N + 1):  # 1부터 N까지 숫자 선택
        if not visited[i]:  # 아직 사용하지 않은 숫자인 경우
            visited[i] = True  # 선택한 숫자를 방문 표시
            result.append(i)  # 숫자 추가
            backtrack()  # 재귀 호출
            result.pop()  # 백트래킹 (원상복구)
            visited[i] = False  # 방문 해제

backtrack()
