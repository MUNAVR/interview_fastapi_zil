from pydantic import BaseModel

class RequestResponseModel(BaseModel):
    name:str
    amount:float
    category:str

    class Config:
        orm_mode = True


class filter(BaseModel):
    month:float

    class Config:
        orm_mode = True

class salary_balance(BaseModel):
    total_salary = float

    class Config:
        orm_mode= True