from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote_plus

# Database Configuration
class Config:
    db_user = "root"  
    db_password = "rootroot"  
    db_host = "localhost"
    db_port = "3306"  
    db_name = "finalProject"  

conf = Config()

# Build the Database URL
SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{conf.db_user}:{quote_plus(conf.db_password)}@"
    f"{conf.db_host}:{conf.db_port}/{conf.db_name}?charset=utf8mb4"
)

# SQLAlchemy Engine and Session
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal will be used to interact with the database in FastAPI routes
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class to define ORM models
Base = declarative_base()

# Dependency for accessing the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
