from flask_restful import Resource, reqparse, request
from utils.extracao_dados import answers_hugging_face, predict_template
from werkzeug.utils import secure_filename
import os
from models.notas import allowed_file
import config

# atributos = reqparse.RequestParser()
# atributos.add_argument('molCaminhoArquivo', type=str, required=True, help="The field 'molCaminhoArquivo' cannot be left blank")

class ExtracaoDados(Resource):

    def post(self):
        f = request.files['file']
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            path = os.path.join(config.UPLOAD_FOLDER, filename)
            answers_hugging_face(path, filename)


        return {'Ok':'Sucesso'},200

