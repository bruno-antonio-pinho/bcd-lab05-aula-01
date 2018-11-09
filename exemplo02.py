# -*- coding: utf-8 -*-

# https://www.pythonsheets.com/notes/python-sqlalchemy.html

from sqlalchemy import create_engine, and_, or_
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine("sqlite:///teste.sqlite")
    Session = sessionmaker(bind=engine)
    session = Session()

    Base = automap_base()
    Base.prepare(engine, reflect=True)

    Contatato = Base.classes.Contato

    lista_de_contatos = session.query(Contatato).all()

    for linha in lista_de_contatos:
        print('Id: {}\t Nome: {}\t Telefone: {}'.format(linha.idContato, linha.nome, linha.telefone))

    bruno = session.query(Contatato).filter(and_(Contatato.nome == 'Andre', Contatato.telefone == '123456789')).first()

    print('O telefone do {} é : {}'.format(bruno.nome, bruno.telefone))

    #bruno.nome = 'Andre'
    #session.commit()
