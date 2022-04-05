from sql_alchemy import banco

class ArquivoStatusModel(banco.Model):
    __tablename__ = 'tblArquivoStatus'

    arsCodigo = banco.Column(banco.Integer, primary_key=True)
    arsDescricao = banco.Column(banco.String(200))

    def __init__(self,
                 arsDescricao):
        self.arsDescricao = arsDescricao


    @classmethod
    def find_status(cls, arsCodigo):
        status = cls.query.filter_by(arsCodigo=arsCodigo).first()
        if status:
            return status.arsDescricao
        return None
