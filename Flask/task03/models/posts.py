from db import db
from datetime import datetime, timezone

# 게시판 테이블 생성
class Post(db.Model):

    __tablename__ = "posts"  # 테이블명 설정
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=lambda: datetime.now(timezone.utc), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False) # user_id를 외래키로 설정
    author = db.relationship('User', back_populates='posts')