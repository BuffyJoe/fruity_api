import database as _database
import models as _models
import sqlalchemy.orm as _orm
import schemas as _schemas

def create_database():
    return _database.Base.metadata.create_all(bind = _database.engine)


def get_db():
    db = _database.SessionLoacl()
    try:
        yield db
    finally:
        db.close()


def get_fruit_by_name(db: _orm.Session, name: str):
    return db.query(_models.Fruit).filter(_models.Fruit.name == name).first()

def get_fruit_by_id(db: _orm.Session, id: int):
    return db.query(_models.Fruit).filter(_models.Fruit.id == id).first()

def create_siting(db: _orm.Session, fruit_id: int, siting: _schemas.create_siting):
    siting= _models.Siting(**siting.dict(), fruit_id = fruit_id)
    print(siting.fruit)
    db.add(siting)
    db.commit()
    db.refresh(siting)
    return siting

def get_siting_by_id(db: _orm.Session, id: int):
    return db.query(_models.Siting).filter(_models.Siting.id == id).first()