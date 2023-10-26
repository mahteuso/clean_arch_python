from sqlalchemy import create_engine
from .obj_string import Obj_conn
from sqlalchemy.orm import sessionmaker

class DbConnectHandler:
    
    def __init__(self) -> None:
        self.__string_conn = Obj_conn().str_conn
        self.session = None
        self.__engine = self.create_engine()
        self.session = None

    def create_engine(self) -> None: 
        engine = create_engine(self.__string_conn)
        return engine

    @property
    def engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close() 