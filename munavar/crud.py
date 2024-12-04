from sqlalchemy.orm import session 
from model import Expense
from schamas import RequestResponseModel,filter,salary_balance

class expense:

    async def create_expense(self, items:RequestResponseModel,db:session):
        db_expense = Expense(items.name,items.amount,items.category)
        db.add(db_expense)
        db.commit()
        db.refresh(db_expense)
        return db_expense
    
    async def get_expense(self,db:session):
        return db.query(Expense).all()
    
    async def filtering(self,month:filter,db:session):
        return db.query(Expense).filter(Expense.category == month).all()
    
    async def balance_amount(self,db:session):
        return db.query(Expense).filter(Expense.amount).all()


