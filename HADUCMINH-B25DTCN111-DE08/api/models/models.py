from sqlalchemy import Column,String,Integer,ForeignKey,Float
from sqlalchemy.orm import relationship
from database import Base

class Category(Base):
    __tablename__='categories'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(50),unique=True,nullable=False)
    
    dishes=relationship('Dishes',back_populates='categories')
class Dishes(Base):
    __tablename__='dishes'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(100),unique=True,nullable=False)
    price=Column(Float,nullable=False)
    category_id=Column(Integer,ForeignKey('categories.id'))
    
    categories=relationship('Category',back_populates='dishes')
