from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MonitoramentoLoteModel(Base):
        __tablename__ = 'tblMonitoramentoLote'

        molCodigo = Column(Integer, primary_key=True)
        molData = Column(DateTime)
        arsCodigo = Column(Integer)
        molCaminhoArquivo = Column(String(200))
        artCodigo = Column(Integer)
