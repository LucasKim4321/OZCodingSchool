# 블록리스트 관리 파일

BLOCKLIST = set()

# 블록리스트에 추가
def add_to_blocklist(jti):  # jti jwt의 고유값
    BLOCKLIST.add(jti)

# 블록리스트에서 제거
def remove_from_blocklist(jti):
    BLOCKLIST.discard(jti)