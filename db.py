from sqlalchemy import Column, String, DateTime, Integer, Boolean
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base() # Base da tabela comum para ORM

class List(Base): # Criando tabela com ORM
    __tablename__ = 'list'
    id = Column(Integer, primary_key=True, autoincrement=True)
    item = Column(String(150), nullable=False)
    when = Column(DateTime, default=datetime.utcnow(), nullable=False)
    done = Column(Boolean, default=False, nullable=False)