from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class NFSeMonitoramento(Base):
    __tablename__ = 'tblNFSeMonitoramentoLote'

    nmCodigo = Column(Integer, primary_key=True)
    mliCodigo = Column(Integer)
    cnpjTomador = Column(String(100))
    scoreCnpjTomador = Column(String(100))
    cnpjPrestador = Column(String(100))
    scoreCnpjPrestador = Column(String(100))
    numeroNota = Column(String(100))
    scoreNumeroNota = Column(String(100))
    dataEmissao = Column(String(100))
    scoreDataEmissao = Column(String(100))
    codigoVerificacao = Column(String(100))
    scoreCodigoVerificacao = Column(String(100))
    codigoServico = Column(String(100))
    scoreCodigoServico = Column(String(100))
    valorTotal = Column(String(100))
    scoreValorTotal = Column(String(100))
    pis = Column(String(100))
    scorePis = Column(String(100))
    enderecoTomador = Column(String(100))
    scoreEnderecoTomador = Column(String(100))
    enderecoPrestador = Column(String(100))
    scoreEnderecoPrestador = Column(String(100))

    def __init__(self,
                 cnpjTomador,
                 cnpjPrestador,
                 numeroNota,
                 dataEmissao,
                 valorTotal, ):
        self.cnpjTomador = cnpjTomador
        self.cnpjPrestador = cnpjPrestador
        self.numeroNota = numeroNota
        self.dataEmissao = dataEmissao
        self.valorTotal = valorTotal