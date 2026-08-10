from database import *
from schemas.schemas import DishesResponse,DishesUpdate
from models.models import *
from fastapi import HTTPException,status
from sqlalchemy.orm import Session
def show_all_by_category(id:int,name:str,db:Session):
    result=db.query(Dishes,Category).filter(Dishes.category_id==id and Category.name==name).all()
    return result
def update_dish(dish:DishesUpdate,id:int,db:Session):
    result=db.query(Dishes).filter(Dishes.id==id).first()
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Món ăn không tồn tại"
        )
    category_result=db.query(Dishes).filter(Dishes.category_id==dish.category_id).first()
    if not category_result:
        raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Danh mục không tồn tại"
                )
    name_result=db.query(Dishes).filter(Dishes.name==dish.name).first()
    if  name_result:
            raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Tên món ăn đã tồn tại"
                    )
    update_data = dish.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(result, key, value)
    db.commit()
    db.refresh(result)
    return result
def delete_dish(id:int,db:Session):
    result=db.query(Dishes).filter(Dishes.id==id).first()
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Món ăn không tồn tại"
        )
    db.delete(result)
    db.commit()
    return result