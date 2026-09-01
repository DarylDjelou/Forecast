import os

from sqlalchemy import create_engine

engine = create_engine(os.environ['POSTGRES_URL'], echo=True)