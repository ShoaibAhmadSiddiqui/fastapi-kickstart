from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import CONFIG

# Create a postgres engine instance
engine = create_engine(
    CONFIG.DB.HOST, pool_size=int(CONFIG.DB.POOL_SIZE), max_overflow=0
)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()
