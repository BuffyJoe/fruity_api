import sqlalchemy as _sql
import database as _database
import sqlalchemy.orm as _orm
from typing import Optional, List
import datetime as _dt

class Fruit(_database.Base):
    __tablename__ = "Fruit"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String, unique=True)
    siting = _orm.relationship("Siting", back_populates="fruit")



class Siting(_database.Base):
    __tablename__ = "Siting"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    fruit_id = _sql.Column(_sql.Integer, _sql.ForeignKey("Fruit.id"))
    fruit = _orm.relationship("Fruit", back_populates="siting")
    condition = _sql.Column(_sql.String)
    latitude = _sql.Column(_sql.Integer)
    longitude = _sql.Column(_sql.Integer)
    