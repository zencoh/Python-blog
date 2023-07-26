from os import getenv
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

#connecting to db using env variables so mysql password is not leaked
#engine manages connection to db
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
#session generates temporary connections for CRUD operations
Session = sessionmaker(bind=engine)
#base helps map models to real SQL tables
Base = declarative_base()