from fastapi import APIRouter,Depends
from database import *
from models.models import *
from schemas.schemas import *
from sqlalchemy.orm import Session
from service.services import *
router=APIRouter(prefix='/restaurant',tags=['Restaurant'])

@router.get("/",response_model=DishesResponse,status_code=200)
def handle_show_all(id:int,name:str,db:Session=Depends(get_db)):
    all=show_all_by_category(id,name,db)
    return all
@router.put("/",response_model=DishesResponse,status_code=200)
def handle_update(dish:DishesUpdate,id:int,db:Session=Depends(get_db)):
    result=update_dish(dish,id,db)
    return result
@router.delete("/",response_model=DishesResponse,status_code=200)
def handle_delete(id:int,db:Session=Depends(get_db)):
    result=delete_dish(id,db)
    return result