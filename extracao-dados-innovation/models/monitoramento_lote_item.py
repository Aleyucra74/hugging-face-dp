from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MonitoramentoLoteItemModel(Base):
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

# def find_all_lote(session):
#     lote_items = session.query(MonitoramentoLoteItemModel).all()
#     if lote_items:
#         return lote_items
#     return None
#
#
# def save_lote_item_molCodigo(session, filename, molCodigo):
#     monitoramento_lote_item = MonitoramentoLoteItemModel(molCodigo=molCodigo,
#                                                          arsCodigo=1,
#                                                          mliCriadoEm=datetime.today(),
#                                                          mliDataFimImportacao=datetime.today(),
#                                                          mliNome=filename)
#
#     session.add(monitoramento_lote_item)
#     session.commit()
#
#
# def save_erro_lote_item(session, molCodigo, erro):
#     session.query(MonitoramentoLoteItemModel).filter(molCodigo=molCodigo) \
#         .first().update({'mliObservacao': erro}, {'arsCodigo': 4})
#
#     session.commit()
#
#
# def save_predict_file(session, mliCodigo, template):
#     monitoramento_lote_item = session.query(MonitoramentoLoteItemModel).filter_by(mliCodigo=mliCodigo).first()
#     monitoramento_lote_item.mliPredict = str(template['text'])
#
#     session.add(monitoramento_lote_item)
#     session.commit()
