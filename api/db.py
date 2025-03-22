
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"
ASYNC_DB_URL = "mysql+aiomysql://root@db:3306/demo?charset=utf8"

# db_engine = create_e1ngine(DB_URL, echo=True)
async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
# db_session = sessionmaker(autocommit = False, autoflush=False, bind=db_engine)

async_session = sessionmaker(bind = async_engine, autocommit=False, autoflush=False, class_=AsyncSession)


Base = declarative_base()

async def get_db():
  async with async_session() as session:
      yield session
