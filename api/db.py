
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
DB_HOST = os.environ.get("DB_HOST", "db")
DB_PORT = os.environ.get("DB_PORT", "3306")

DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"
ASYNC_DB_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/demo?charset=utf8"

# 同期実行
# db_engine = create_e1ngine(DB_URL, echo=True)
# db_session = sessionmaker(autocommit = False, autoflush=False, bind=db_engine)

# 非同期実行
async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
async_session = sessionmaker(bind = async_engine, autocommit=False, autoflush=False, class_=AsyncSession)


Base = declarative_base()

async def get_db():
  async with async_session() as session:
      yield session
