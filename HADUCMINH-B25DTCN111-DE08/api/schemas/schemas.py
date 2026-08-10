from pydantic import BaseModel,Field

class DishesResponse(BaseModel):
    id:int
    name:str
    price:float
class DishesUpdate(BaseModel):
    name:str=Field(...,gt=0,lt=100)
    price:float=Field(...,gt=0)
    category_id:int=Field(...)