from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:fastapi_password@localhost:33060/fastapi_db"

# sqlalchemy create_engine사용
engine = create_engine(DATABASE_URL)
SessionFactory = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    bind=engine,
)

# session: 데이터베이스 접속 단위

# 기본 부모 클래스
Base = declarative_base()

# Dependency Injection(=의존성 주입)
# generator 문법
def get_session():
    session = SessionFactory()
    try:
        yield session # 중간 return
    finally:
        session.close()

