from fastapi import FastAPI , status,HTTPException,Depends
from db import engin,Base,get_db
from model import Expense
from schamas import RequestResponseModel,filter,salary_balance
from crud import expense
from typing import Annotated
from sqlalchemy.orm import session

crud=expense()
app=FastAPI()
db_dependency = Annotated[session,Depends(get_db)]
Base.meta.create_all(bind=engin)

@app.post("/create_expense/",status_code=status.HTTP_201_CREATED)
async def create_expense(items:RequestResponseModel,db:db_dependency):
    return crud.create_expense(items,db)

@app.get("/get_all_expense/")
async def get_all(db:db_dependency):
    return crud.get_expense(db)

@app.get("/expense_monthly/")
async def expense_monthly(month:filter,db:db_dependency):
    return await crud.filtering(month,db)

@app.get("/balance_amount/")
async def balance_amount(db:db_dependency):
    return crud.balance_amount(db)