from sql_alchemy import banco
import uuid
from datetime import datetime

class RequisicaoModel(banco.Model):

    __tablename__ = 'tblRequisicaoMonitoramentoLote'

    rmlCodigo = banco.Column(banco.Integer, primary_key=True)
    molCodigo = banco.Column(banco.Integer)
    rmlService_ID = banco.Column(banco.String(500))
    arsCodigo = banco.Column(banco.Integer)
    rmlDataInicioVerificacao = banco.Column(banco.DateTime)
    rmlDataFimVerificacao = banco.Column(banco.DateTime)
    rmlMensagemErro = banco.Column(banco.String(200))

    def __init__(self,
                 molCodigo,
                 rmlService_ID,
                 arsCodigo,
                 rmlDataInicioVerificacao):
        self.molCodigo = molCodigo
        self.rmlService_ID = rmlService_ID
        self.arsCodigo = arsCodigo
        self.rmlDataInicioVerificacao = rmlDataInicioVerificacao

    def json(self):
        return {
            'rmlCodigo': self.rmlCodigo,
            'molCodigo': self.molCodigo,
            'rmlService_ID': self.rmlService_ID,
            'arsCodigo': self.arsCodigo,
            'rmlDataInicioVerificacao': self.rmlDataInicioVerificacao,
            'rmlDataFimVerificacao': self.rmlDataFimVerificacao,
            'rmlMensagemErro': self.rmlMensagemErro
        }

    @classmethod
    def find_requisicao(cls, rmlService_ID):
        req = cls.query.filter_by(rmlService_ID=rmlService_ID).first()
        if req:
            return req
        return None

    @classmethod
    def find_by_molCodigo(cls, molCodigo):
        req = cls.query.filter_by(molCodigo=molCodigo).first()
        if req:
            return req
        return None

    @classmethod
    def save_requisicao_monitoramento(self, molCodigo):
        req = RequisicaoModel(molCodigo=molCodigo,
                              rmlService_ID=str(uuid.uuid4()),
                              arsCodigo=1,
                              rmlDataInicioVerificacao=datetime.today())

        banco.session.add(req)
        banco.session.commit()

        return req.rmlService_ID


    @classmethod
    def delete_requisicao(self, req):
        banco.session.delete(req)
        banco.session.commit()