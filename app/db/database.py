"""
初始化MySQL数据库
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:jhqwe321@127.0.0.1/jh_cross'

Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URI)
LocalSession = sessionmaker(bind=engine,autoflush=False,autocommit=False)
