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
        if nome and re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) and len(senha)>=8 and not all(ord(senha[i+1]) == ord(senha[i]) + 1 for i in range(len(senha) - 1)):
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
    def alterar_email(cls, old_email, senha, new_email):
        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', new_email):
            for email in session.query(Users.email).all()[0]:
                if new_email == email:
                    return "Email já cadastrado"
                elif old_email == email and senha == session.query(Users.senha).filter(Users.email == old_email).all()[0][0]:
                    session.query(Users).filter(Users.email == old_email).update({Users.email: new_email})
                    session.commit()
                    session.close()
                    return "Email alterado com sucesso"
                else:
                    "Email ou senha incorreto"
        else:
            return "Formato de e-mail inválido"
        
                    
                
                
    
    @classmethod
    def alterar_senha(cls):
        pass
    
    @classmethod
    def excluir():
        pass
    
print(ControllerCadastro.alterar_email(old_email="abc@hotmail.cos", senha="paula", new_email="abc@hotmail.coks"))

Base.metadata.create_all(engine)