from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MonitoramentoLoteItemOCR(Base):
    __tablename__ = 'tblMonitoramentoLoteItem'

    mliCodigo = Column(Integer, primary_key=True)
    molCodigo = Column(Integer)
    mliMensagemStatus = Column(String(200))
    mliObservacao = Column(String(200))
    arsCodigo = Column(Integer)
    mliCriadoEm = Column(DateTime)
    mliDataFimImportacao = Column(DateTime)
    mliNome = Column(String(1000))
    mliPredict = Column(String(60))