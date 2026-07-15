from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
Database_URL = "mysql+pymysql://root:Prabha%4020_04@localhost:3306/task_db"
engine = create_engine(Database_URL)
SessionLocal = sessionmaker(autocommit=False, bind=engine, autoflush=False)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()