# Model -> Table 생성
# 게시글 - board
# 유저 - user

from db import db  # db = SQLAlchemy()

# 유저 테이블 생성
class User(db.Model):

    __tablename__ = "users"  # 테이블명 설정

    # 컬럼 설정
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # varchar(100)
    email = db.Column(db.String(100), nullable=False, unique=True)
    boards = db.relationship('Board', back_populates='author', lazy='dynamic') # 역참조. lazy='dynamic' 필요할 때만 쿼리를 실행

# 게시판 테이블 생성
class Board(db.Model):

    __tablename__ = "boards"  # 테이블명 설정
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False) # user_id를 외래키로 설정
    author = db.relationship('User', back_populates='boards')