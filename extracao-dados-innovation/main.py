import os
import config
from models.monitoramento_lote_item import MonitoramentoLoteItemModel
from utils.extracao_dados import answers_hugging_face,predict_template
from utils.notas import transform_nota_text

def executar():
    os.system('clear')
    print('')
    print('---------------------------------------------------------------------------')
    print(f'Iniciando extração de dados console')

    try:
        print(f'Obtendo as notas pendentes para extração de dados')
        lista_pendentes = MonitoramentoLoteItemModel.find_all_lote()

        print(f'Iniciando predict da nota')
        for arquivo in lista_pendentes:
            text = transform_nota_text(os.path.join(config.UPLOAD_FOLDER, arquivo.mliNome))

            template = predict_template(text)
            MonitoramentoLoteItemModel.save_predict_file(arquivo.mliCodigo,template)

    except Exception as e:
        print(f'Não foi possível extrair os dados das notas. Erro: {str(e)}')





