from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ambient_variable import CONN
from model import Users
import re

engine = create_engine(CONN, echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine) # Criando uma sessão baseada no engine
session = Session()

class ControllerCadastro():
    
    @classmethod
    def cadastrar(cls, nome=None, email=None, senha=None):
        if nome and re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            user = Users(nome=nome, email=email, senha=senha)
            session.add(user)
            session.commit()
            session.close()
            return "Usuário cadastrado com sucesso"
        else:
            return "Erro ao cadastrar usuário"

    @classmethod
    def alterar_nome(cls):
        pass
    
    @classmethod
    def alterar_email(cls):
        pass
    
    @classmethod
    def alterar_senha(cls):
        pass
    
    @classmethod
    def excluir():
        pass
    
print(ControllerCadastro.cadastrar(nome="abc", email="abc@hotmail.com", senha="paula"))

Base.metadata.create_all(engine)