import os
from flask_restful import Resource, request
from werkzeug.utils import secure_filename
from flask import jsonify
from flask_jwt_extended import jwt_required
from models.notas import allowed_file, transform_nota_text, predict_nota, convert_predict_to_municipio
import config

class Upload(Resource):

    def post(self):
            f = request.files['file']
            if f and allowed_file(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(config.UPLOAD_FOLDER + 'a_notas_fiscais/', filename))
                textfile = transform_nota_text(filename)
                predict = predict_nota(textfile)

                return jsonify({"predict": convert_predict_to_municipio(int(predict))})