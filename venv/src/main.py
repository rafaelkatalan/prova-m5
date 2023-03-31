from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, sessionmaker
from models.base import Base
from models.jogoEletronico import Pessoa


engine = create_engine("sqlite+pysqlite:///jogo.db", echo=True)

Session = sessionmaker(bind = engine)
session = Session()

Base.metadata.create_all(engine)


jogo1 = jogoEletronico(nome= "DEAD SPACE REMAKE", plataforma= "PS5", preco= 350.00, quantidade=10)

session.add(jogo1)
session.commit()

session = Session(engine)

def add(name, plat,price, quant):
    jogo1 = jogoEletronico(nome=name, plataforma=plat, preco= price, quantidade=quant)

    session.add(jogo1)
    session.commit()

    session = Session(engine)

def read():
    
    stmt = select(jogoEletronico)

    for jogoEletronico in session.scalars(stmt):
         print(jogoEletronico)