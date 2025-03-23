from sqlalchemy.exc import OperationalError, InternalError
from sqlalchemy import create_engine, text

from api.db import DB_HOST, DB_PASSWORD, DB_PORT, DB_USER
from api.models.task import Base


DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}?charset=utf8"
DEMO_DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/demo?charset=utf8"

db_engine = create_engine(DEMO_DB_URL, echo=True)

def database_exists():
  # 接続を試みることでdemoデータベースの存在を確認
  try:
    db_engine.connect()
    return True
  except (OperationalError, InternalError) as e:
    print(e)
    print("database doed not exist")
    return False
  
def create_database():
  if not database_exists():
    # demoデータベースが存在しなければ作成
    root = create_engine(DB_URL, echo=True)
    with root.connect() as conn:
      conn.execute(text("CREATE DATABASE demo"))
    print("created database")
    
  # DBモデルをもとにテーブルを作成
  Base.metadata.creata_all(bind=db_engine)
  print("created tables")
  
if __name__ == "__main__":
  create_database()
  

# def reset_database():
#   Base.metadata.drop_all(bind=db_engine)
#   Base.metadata.create_all(bind=db_engine)
  
# if __name__ == "__main__":
#   reset_database()