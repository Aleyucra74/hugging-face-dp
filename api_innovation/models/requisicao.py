from sql_alchemy import banco
import uuid
from datetime import datetime
from models.arquivo_status import ArquivoStatusModel
import json

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

        data_inicio = 'Sem Data'
        data_fim = 'Sem Data'

        if self.rmlDataInicioVerificacao is not None:
            data_inicio = "{}-{}-{}".format(self.rmlDataInicioVerificacao.year,
                                            self.rmlDataInicioVerificacao.month,
                                            self.rmlDataInicioVerificacao.day)

        if self.rmlDataFimVerificacao is not None:
            data_fim = "{}-{}-{}".format(self.rmlDataFimVerificacao.year,
                                            self.rmlDataFimVerificacao.month,
                                            self.rmlDataFimVerificacao.day)
        return {
            # 'rmlCodigo': self.rmlCodigo,
            # 'molCodigo': self.molCodigo,
            'service_id': self.rmlService_ID,
            'status': ArquivoStatusModel.find_status(self.arsCodigo),
            'data_inicio_verificacao': data_inicio,
            'data_fim_verificacao': data_fim,
            'mensagem_erro': self.rmlMensagemErro
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
    def find_req_excel(cls, molCodigo):
        lista_excel = banco.session.execute('innovation_GetRequisicaoExcel_s').all()
        if lista_excel:
            return lista_excel
        return None


    @classmethod
    def delete_requisicao(self, req):
        banco.session.delete(req)
        banco.session.commit()