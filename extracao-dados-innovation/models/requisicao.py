from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class RequisicaoModel(Base):

    __tablename__ = 'tblRequisicaoMonitoramentoLote'

    rmlCodigo = Column(Integer, primary_key=True)
    molCodigo = Column(Integer)
    rmlService_ID = Column(String(500))
    arsCodigo = Column(Integer)
    rmlDataInicioVerificacao = Column(DateTime)
    rmlDataFimVerificacao = Column(DateTime)
    rmlMensagemErro = Column(String(200))

