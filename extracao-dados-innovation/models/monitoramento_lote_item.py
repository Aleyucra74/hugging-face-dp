from sql_alchemy import banco
from datetime import datetime
from zipfile import ZipFile
import config

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
    mliPredict = banco.Column(banco.String(60))

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

    @classmethod
    def find_all_lote(cls):
        lote_items = cls.query.all()
        if lote_items:
            return lote_items
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
    def save_predict_file(cls, mliCodigo, template):
        monitoramento_lote_item = cls.query.filter_by(mliCodigo=mliCodigo).first()
        monitoramento_lote_item.mliPredict = str(template['text'])

        banco.session.add(monitoramento_lote_item)
        banco.session.commit()
