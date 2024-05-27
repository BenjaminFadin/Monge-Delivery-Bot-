from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://{}:{}@localhost:5432/{}'.format('postgres', '5432', 'test'))
Session = sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()

