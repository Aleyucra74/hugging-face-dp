from sql_alchemy import banco

class MonitoramentoLoteModel(banco.Model):
    __tablename__ = 'tblMonitoramentoLote'

    molCodigo = banco.Column(banco.Integer, primary_key=True)
    molData = banco.Column(banco.DateTime)
    arsCodigo = banco.Column(banco.Integer)
    molCaminhoArquivo = banco.Column(banco.String(200))
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

    @classmethod
    def find_lote(cls, molCodigo):
        user = cls.query.filter_by(molCodigo=molCodigo).first()
        if user:
            return user
        return None

