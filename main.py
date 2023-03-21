from fastapi import FastAPI, Depends, HTTPException, status
import database as _db
import sqlalchemy.orm as _orm
from typing import List
import models as _models
import schemas as _schemas
import services as _services
import datetime as _dt

app = FastAPI()

_services.create_database()





@app.get("/fruity", response_model=List[_schemas.Fruit])
async def all_fruits(db: _orm.Session=Depends(_services.get_db)):
    fruits =  db.query(_models.Fruit).offset(0).limit(10).all()
    return fruits

@app.get("/fruity/{fruit_name}", response_model=_schemas.Fruit)
def get_single_fruit(fruit_name:str, db:_orm.Session=Depends(_services.get_db)):
    fruit = _services.get_fruit_by_name(db=db, name = fruit_name)
    if fruit is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item can not be found in the database")
    return fruit

@app.delete("/fruity/delete/{fruit_name}")
def delete_fruit(fruit_name: str, db : _orm.Session=Depends(_services.get_db)):
    fruit = _services.get_fruit_by_name(db=db, name=fruit_name)
    db.delete(fruit)
    db.commit()
    return f'{fruit.name} has been successfully defeated'

@app.delete("/fruity/delete/siting/{siting_id}")
def delete_siting(siting_id : int, db : _orm.Session=Depends(_services.get_db)):
    siting = _services.get_siting_by_id(db=db, id=siting_id)
    db.delete(siting)
    db.commit()
    return f'siting with id:{siting.id} has been successfully defeated'


@app.post("/fruity")
async def add_fruit(fruit: _schemas.create_fruit, db:_orm.Session=Depends(_services.get_db) ):
    fruit_name = fruit.name
   
    db_fruit = _services.get_fruit_by_name(db=db, name=fruit_name)
    if db_fruit :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Already Exists try adding a siting instead')
    new_fruit= _models.Fruit(**fruit.dict())
    db.add(new_fruit)
    db.commit()
    db.refresh(new_fruit)
    return new_fruit

@app.post("/fruity/{fruit_id}/sitings/")
def create_siting(fruit_id: int, siting: _schemas.create_siting, db:_orm.Session=Depends(_services.get_db)):
    db_fruit = _services.get_fruit_by_id(db=db, id=fruit_id)
    if db_fruit is None:
       raise HTTPException(status_code=404, detail="Fruit not found")   
    siting= _models.Siting(**siting.dict(), fruit_id = fruit_id)
    print(siting.condition)
    db.add(siting)
    db.commit()
    db.refresh(siting)
    return siting

