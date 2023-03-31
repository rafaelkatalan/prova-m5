from sqlalchemy import create_engine
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