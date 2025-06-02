# models.py
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Example credentials for PostgreSQL (can switch to SQLite if preferred)
import os

DB_USER = os.getenv('DB_USER', 'default_user')
DB_PASS = os.getenv('DB_PASS', 'default_password')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'testdb')
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# For SQLite instead: DATABASE_URL = "sqlite:///posts.db"

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)

# Set up the engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)