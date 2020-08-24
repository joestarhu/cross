"""
初始化MySQL数据库
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

Base = declarative_base()
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
LocalSession = sessionmaker(bind=engine,autoflush=False,autocommit=False)
