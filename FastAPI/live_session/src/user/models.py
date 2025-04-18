from datetime import datetime

from sqlalchemy import Integer, Column, String, DateTime

from database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(16))
    password = Column(String(60))
    created_at = Column(DateTime, default=datetime.now)

# Django: model -> table
# python manage.py makemigrations -> migration 파일 -> python manage.py migrate

# Django에는 ORM + Migration 기능

# sqlalchemy는 ORM만 지원
# migration 하려면 Alembic

# DDL: CREATE TABLE