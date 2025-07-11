from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base  

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:consultadd!@Localhost/TodosApplication"


engine = create_engine(SQLALCHEMY_DATABASE_URL)

#instance of a db session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()  #creates a db model
