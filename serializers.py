from flask_sqlalchemy import SQLAlchemy
from flask import json
from sqlalchemy.orm.attributes import QueryableAttribute
from app import app

db = SQLAlchemy(app)

class MySerializer(db.Model):

    