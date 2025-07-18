from sqlalchemy.exc import SQLAlchemyError

from abc import ABC, abstractmethod

from app.db.get_db import get_db
from app.db.model import Graph

class GraphBase(ABC):
    @abstractmethod
    def add_to_graph(self, name_graph : str, graph : str) -> None:
        pass

    @abstractmethod
    def search_by_name(self, name_graph : str) -> str:
        pass

class GraphWork(GraphBase):
    def add_to_graph(self, name_graph : str, graph : str):
        with get_db() as db:
            try:
                grh = Graph(name=name_graph, equation=graph)
            
                db.add(grh)
                db.commit()
            
            except SQLAlchemyError as e:
                db.rollback()
                return str(e)
            
    def search_by_name(self, name_graph : str) -> str:
        with get_db() as db:
            try:
                expr = db.query(Graph).filter(Graph.name == name_graph).first()

                if expr == None:
                    raise SQLAlchemyError('Name innocorrect or there is no such entry')

                return expr.equation
            except SQLAlchemyError as e:
                return f'Not found. detail: {e}'