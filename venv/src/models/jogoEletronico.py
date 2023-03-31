from models.base import Base
from sqlalchemy import Column, Integer, String, REAL

class jogoEletronico(Base):
    __tablename__ = "Jogo"
    id = Column(String, primary_key=True)
    nome=Column(String)
    plataforma=Column(Integer)
    preco=Column(REAL)
    quantidade=Column(Integer)

    def __repr__(self) -> str:
      return f"jogoEletronico(id={self.id}, nome={self.nome}, plataforma={self.plataforma}, preco={self.preco}, quantidade={self.quantidade})"
