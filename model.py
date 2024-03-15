from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from ambient_variable import CONN
    
# Criando o banco de dados caso não exista
engine = create_engine(CONN, echo=False)
if not database_exists(engine.url):
    create_database(engine.url)
    
Base = declarative_base()
Session = sessionmaker(bind=engine) # Criando uma sessão baseada no engine
session = Session()

class Users(Base):
    __tablename__ = 'Users'
    nome = Column(String(50), nullable=False)
    email = Column(String(100), primary_key=True)
    senha = Column(String(100), nullable=False)
    
    def __repr__(self):
        return f"User(nome={self.nome}, email={self.email}, senha={self.senha})"


if __name__ == '__main__':
    print(session.query(Users).all())
    
    Base.metadata.create_all(engine)