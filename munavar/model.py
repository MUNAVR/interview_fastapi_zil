from sqlalchemy import Integer,String,Column,Float
from db import Base

class Expense(Base):
    __tablename__ = "expense"

    id = Column(Integer(primary_key=True, index=True))
    name = Column(String(index=True))
    amount = Column(Float(index=True))
    category = Column(String(index=True))