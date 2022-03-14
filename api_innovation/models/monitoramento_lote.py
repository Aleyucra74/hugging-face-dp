from sql_alchemy import banco
from datetime import datetime
from models.requisicao import RequisicaoModel

class MonitoramentoLoteModel(banco.Model):
    __tablename__ = 'tblMonitoramentoLote'

    molCodigo = banco.Column(banco.Integer, primary_key=True)
    molData = banco.Column(banco.DateTime)
    arsCodigo = banco.Column(banco.Integer)
    molCaminhoArquivo = banco.Column(banco.String(200))
    molNomeFisico = banco.Column(banco.String(200))
    molNomeLogico = banco.Column(banco.String(200))
    artCodigo = banco.Column(banco.Integer)

    def __init__(self,
                 molData,
                 arsCodigo,
                 molCaminhoArquivo,
                 artCodigo):
        self.molData = molData
        self.arsCodigo = arsCodigo
        self.molCaminhoArquivo = molCaminhoArquivo
        self.artCodigo = artCodigo

    def json(self):
        return {
            'molCodigo': self.molCodigo,
            'molData': self.molData,
            'arsCodigo': self.arsCodigo,
            'molCaminhoArquivo': self.molCaminhoArquivo,
            'artCodigo': self.artCodigo
        }

    @classmethod
    def find_lote(cls, molCodigo):
        user = cls.query.filter_by(molCodigo=molCodigo).first()
        if user:
            return user
        return None

    @classmethod
    def save_lote(self, filename):
        monitoramento_lote = MonitoramentoLoteModel(molCaminhoArquivo=filename,
                                                    molData=datetime.today(),
                                                    arsCodigo=1,
                                                    artCodigo=3)

        banco.session.add(monitoramento_lote)
        banco.session.commit()

        codigo = banco.session.execute('innovation_ContarMonitoramentoLote_s').first()

        token = RequisicaoModel.save_requisicao_monitoramento(codigo)
        return token


    @classmethod
    def delete_user(self, user):
        banco.session.delete(user)
        banco.session.commit()