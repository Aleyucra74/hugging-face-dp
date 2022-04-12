from flask_restful import Resource, reqparse, inputs
from models.requisicao import RequisicaoModel
from utils.excel import import_excel, import_excel_array
from flask import send_file
from flask_jwt_extended import jwt_required

atributos = reqparse.RequestParser()
atributos.add_argument('molCodigo', type=int, required=True, help="The field 'molCodigo' cannot be left blank")
atributos.add_argument('rmlService_ID', type=int, required=True, help="The field 'rmlService_ID' cannot be left blank")
atributos.add_argument('arsCodigo', type=int, required=True, help="The field 'arsCodigo' cannot be left blank")
atributos.add_argument('rmlDataInicioVerificacao', type=inputs.datetime_from_iso8601 , required=True, help="The field 'rmlDataInicioVerificacao' cannot be left blank")

class Requisicao(Resource):

    # @jwt_required()
    def get(self, service_ID):
        req = RequisicaoModel.find_requisicao(service_ID)
        if req:
            if req.arsCodigo == 3:
                requisicao_excel = RequisicaoModel.find_req_excel(req.molCodigo)
                if req:
                    filename = import_excel(requisicao_excel)
                    return send_file(filename,attachment_filename='requisicaoRelatorio.xlsx')
                return {'message': 'request not found'}, 404

            return req.json()

        return {'message': 'request not found'}, 404

