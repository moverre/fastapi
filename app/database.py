from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2, time
from psycopg2.extras import RealDictCursor
from .config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# for reference; not needed anymore
# while True:

#     try:
#         conn = psycopg2.connect(host='localhost',database='fastapi',
#         user='postgres',password='geheim',cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesfull.")
#         break
#     except Exception as error:
#         print("Connection to database failed.")
#         print("Error: ", error)
#         time.sleep(3)
