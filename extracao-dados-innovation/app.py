from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config
import os
import utils.extracao_dados as extracao_dados
from models.monitoramento_lote_item import MonitoramentoLoteItemModel
from models.monitoramento_lote import MonitoramentoLoteModel
from models.requisicao import RequisicaoModel
from models.nfse_monitoramento import NFSeMonitoramento

url_db = quote_plus(config.PARAMS)
engine = create_engine('mssql+pyodbc:///?odbc_connect=%s' % url_db)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def update_requisicao(molCodigo):
    lote = session.query(RequisicaoModel) \
        .filter_by(molCodigo=molCodigo).first()
    lote.arsCodigo = 3

    session.add(lote)
    session.commit()

def update_monitoramento_lote(molCodigo):
    lote = session.query(MonitoramentoLoteModel) \
        .filter_by(molCodigo=molCodigo).first()
    lote.arsCodigo = 3

    session.add(lote)
    session.commit()

def update_monitoramento_lote_item(mliCodigo):
    lote_item = session.query(MonitoramentoLoteItemModel) \
        .filter_by(mliCodigo=mliCodigo).first()
    lote_item.arsCodigo = 3

    session.add(lote_item)
    session.commit()


if __name__ == "__main__":
    #cria todas as tabelas
    # Base.metadata.create_all(engine)
    session = Session()

    print('')
    print('---------------------------------------------------------------------------')
    print(f'Iniciando extração de dados console')

    print(f'Obtendo as notas pendentes para extração de dados')
    lista_pendentes = session.query(MonitoramentoLoteItemModel).filter_by(arsCodigo=1).all()

    if lista_pendentes is None:
        print(f'Não existem notas para extração de dados')
    else:
        print(f'Iniciando predict da nota')

        for arquivo in lista_pendentes:
            try:
                #Salvar no banco
                text = extracao_dados.transform_nota_text(os.path.join(config.PATH_DESCOMPACTADOS, arquivo.mliNome),
                                                          arquivo.mliNome)

                municipio = extracao_dados.return_predict_mun(text)
                # template = extracao_dados.predict_template(municipio)

                if municipio != None or municipio != {}:
                    lote_item = session.query(MonitoramentoLoteItemModel)\
                        .filter_by(mliCodigo=arquivo.mliCodigo).first()
                    # lote_item.mliPredict = str(template['text'])
                    lote_item.mliPredict = str(municipio)

                    session.add(lote_item)
                    session.commit()

                nfse_txt = extracao_dados.answers_hugging_face(os.path.join(config.PATH_DESCOMPACTADOS, arquivo.mliNome),
                                                          arquivo.mliNome)
                nfse_predict = NFSeMonitoramento(None,None,None,None,None)
                nfse_predict.mliCodigo = arquivo.mliCodigo

                for pergunta in nfse_txt:
                    if pergunta.questao == 'Qual o CNPJ do Tomador de Serviço?':
                       nfse_predict.cnpjTomador = pergunta.resultado
                       nfse_predict.scoreCnpjTomador = str(pergunta.score)

                    elif pergunta.questao == 'Qual o CNPJ do Prestador de Serviço?':
                        nfse_predict.cnpjPrestador = pergunta.resultado
                        nfse_predict.scoreCnpjTomador = str(pergunta.score)

                    elif pergunta.questao == 'Qual o Número da Nota/Nº ?':
                        nfse_predict.numeroNota = pergunta.resultado
                        nfse_predict.scoreNumeroNota = str(pergunta.score)

                    elif pergunta.questao == 'Qual a Data de Emissão da Nota Fiscal?':
                        nfse_predict.dataEmissao = pergunta.resultado
                        nfse_predict.scoreDataEmissao = str(pergunta.score)

                    elif pergunta.questao == 'Qual o Código de Verificação?':
                        nfse_predict.codigoVerificacao = pergunta.resultado
                        nfse_predict.scoreCodigoVerificacao = str(pergunta.score)

                    elif pergunta.questao == 'Qual o Código de Serviço?':
                        nfse_predict.codigoServico = pergunta.resultado
                        nfse_predict.scoreCodigoServico = str(pergunta.score)

                    elif pergunta.questao == 'Qual o Valor Total do serviço?':
                        nfse_predict.valorTotal = pergunta.resultado
                        nfse_predict.scoreValorTotal = str(pergunta.score)

                    elif pergunta.questao == 'Qual o Valor dos PIS?':
                        nfse_predict.pis = pergunta.resultado
                        nfse_predict.scorePis = str(pergunta.score)

                    elif pergunta.questao == 'Qual o Enderço do Tomador?':
                        nfse_predict.enderecoTomador = pergunta.resultado
                        nfse_predict.scoreEnderecoTomador = str(pergunta.score)

                    elif pergunta.questao == 'Qual o Enderço do Prestador?':
                        nfse_predict.enderecoPrestador = pergunta.resultado
                        nfse_predict.scoreEnderecoPrestador = str(pergunta.score)

                session.add(nfse_predict)
                session.commit()

                update_monitoramento_lote_item(arquivo.mliCodigo)
                update_monitoramento_lote(arquivo.molCodigo)
                update_requisicao(arquivo.molCodigo)



            except Exception as e:
                print(f'Não foi possível extrair os dados das notas. Erro: {str(e)}')
                lote_item = session.query(MonitoramentoLoteItemModel).filter_by(mliCodigo=arquivo.mliCodigo).first()
                lote_item.mliObservacao = str(e)
                lote_item.arsCodigo = 4

                session.add(lote_item)
                session.commit()

    session.close()