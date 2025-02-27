from db import db

# 유저 테이블 생성
class User(db.Model):

    __tablename__ = "users"  # 테이블명 설정

    # 컬럼 설정
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # varchar(100)
    email = db.Column(db.String(100), nullable=False, unique=True)
    posts = db.relationship('Post', back_populates='author', lazy='dynamic') # 역참조. lazy='dynamic' 필요할 때만 쿼리를 실행
