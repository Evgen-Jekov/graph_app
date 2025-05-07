from app.db.get_db import base
from sqlalchemy import Integer, Text, Column, String

class Graph(base):
    __tablename__ = 'graphs'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(256), unique=True, nullable=False)
    equation = Column(Text, nullable=False)