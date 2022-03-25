from sql_alchemy import banco
from datetime import datetime

class MonitoramentoLoteItemModel(banco.Model):
    __tablename__ = 'tblMonitoramentoLoteItem'

    mliCodigo = banco.Column(banco.Integer, primary_key=True)
    molCodigo = banco.Column(banco.Integer)
    mliMensagemStatus = banco.Column(banco.String(200))
    mliObservacao = banco.Column(banco.String(200))
    arsCodigo = banco.Column(banco.Integer)
    mliCriadoEm = banco.Column(banco.DateTime)
    mliDataFimImportacao = banco.Column(banco.DateTime)
    mliNome = banco.Column(banco.String(1000))

    def __init__(self,
                 molCodigo,
                 arsCodigo,
                 mliCriadoEm,
                 mliDataFimImportacao,
                 mliNome):
        self.molCodigo = molCodigo
        self.arsCodigo = arsCodigo
        self.mliCriadoEm = mliCriadoEm
        self.mliDataFimImportacao = mliDataFimImportacao
        self.mliNome = mliNome

    def json(self):
        return {
            'Código Lote': self.molCodigo,
            'Criado Em': self.mliCriadoEm,
            'arsCodigo': self.arsCodigo,
            'Caminho Arquivo': self.molCaminhoArquivo,
            'Data Fim Importacao': self.mliDataFimImportacao,
            'Nome': self.mliNome
        }

    @classmethod
    def find_lote_item(cls, molCodigo):
        user = cls.query.filter_by(molCodigo=molCodigo).first()
        if user:
            return user
        return None

    @classmethod
    def save_lote_item(self, filename, molCodigo):
        monitoramento_lote_item = MonitoramentoLoteItemModel(molCodigo=molCodigo,
                                                    arsCodigo=1,
                                                    mliCriadoEm=datetime.today(),
                                                    mliDataFimImportacao=datetime.today(),
                                                    mliNome=filename)

        banco.session.add(monitoramento_lote_item)
        banco.session.commit()

    @classmethod
    def save_lote_item_zip(self, filename, molCodigo):
        monitoramento_lote_item = MonitoramentoLoteItemModel(molCodigo=molCodigo,
                                                    arsCodigo=1,
                                                    mliCriadoEm=datetime.today(),
                                                    mliDataFimImportacao=datetime.today(),
                                                    mliNome=filename)

        banco.session.add(monitoramento_lote_item)
        banco.session.commit()