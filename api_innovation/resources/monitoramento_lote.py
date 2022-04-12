from flask_restful import Resource, reqparse, request
from models.monitoramento_lote import MonitoramentoLoteModel
from werkzeug.utils import secure_filename
import os
from models.notas import allowed_file
import config

atributos = reqparse.RequestParser()
atributos.add_argument('molCaminhoArquivo', type=str, required=True, help="The field 'molCaminhoArquivo' cannot be left blank")


class MonitoramentoLote(Resource):

    # @jwt_required()
    def post(self):
        f = request.files['file']
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(config.UPLOAD_FOLDER +filename))
            token = MonitoramentoLoteModel.save_lote(filename)

        return {'Service ID':token},200

