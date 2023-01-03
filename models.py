from sqlalchemy import Boolean, Column, Integer, String
from database import Base


class Tarefas(Base):
    __tablename__ = "tarefas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    descricao = Column(String)
    prioridade = Column(Integer)
    completo = Column(Boolean, default=False)