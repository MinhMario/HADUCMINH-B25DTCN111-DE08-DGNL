from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

DATABASE_URL='mysql+pymysql://root:Minh01052007.@localhost:3306/restaurantdb'
engine=create_engine(DATABASE_URL)
LocalSession=sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base=declarative_base()

def get_db():
    db=LocalSession()
    try:
        yield db
    finally:
         db.close()