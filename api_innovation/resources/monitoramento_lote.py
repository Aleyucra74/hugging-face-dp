from flask_restful import Resource, reqparse, inputs
from models.requisicao import RequisicaoModel
from flask_jwt_extended import jwt_required

atributos = reqparse.RequestParser()
atributos.add_argument('molCodigo', type=int, required=True, help="The field 'molCodigo' cannot be left blank")
atributos.add_argument('molData', type=inputs.datetime_from_iso8601 , required=True, help="The field 'molData' cannot be left blank")
atributos.add_argument('arsCodigo', type=int, required=True, help="The field 'arsCodigo' cannot be left blank")
atributos.add_argument('molCaminhoArquivo', type=str, required=True, help="The field 'molCaminhoArquivo' cannot be left blank")
atributos.add_argument('artCodigo', type=int, required=True, help="The field 'artCodigo' cannot be left blank")


class MonitoramentoLote(Resource):

    @jwt_required()
    def get(self, service_ID):
        req = RequisicaoModel.find_requisicao(service_ID)
        if req:
            return req.json()
        return {'message': 'request not found'}, 404

