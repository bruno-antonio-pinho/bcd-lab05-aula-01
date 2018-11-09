# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Integer, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///lab05-ex04.sqlite")
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'Pessoa'
    idPessoa = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)

    def __init__(self, nome):
        self.nome = nome

class Telefone(Base):
    __tablename__ = 'Telefone'
    idTelefone = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(String)
    idPessoa = Column(Integer, ForeignKey('Pessoa.idPessoa'))
    pessoa = relationship('Pessoa', backref='Telefone')

    def __init__(self, numero, pessoa):
        self.numero = numero
        self.pessoa = pessoa

if __name__ == '__main__':

    # Gerando o esquema do banco de dados
    Base.metadata.create_all(engine)

    session = Session()

    #bruno = Pessoa('Bruno')

    #session.add(bruno)

    ana = Pessoa('Ana')
    pedro = Pessoa('Pedro')
    juca = Pessoa('Juca')
    julia = Pessoa('Julia')

    session.add(ana)

    juca_telefone = Telefone('(48) 98181-1010', juca)
    session.add(juca)
    session.add(juca_telefone)

    session.commit()
    session.close()