from flask import Flask, jsonify
from flask_restful import  Api
from flask_jwt_extended import JWTManager
import pyodbc

import config
from resources.notas import Upload
from resources.usuario import User, UserRegister, UserLogin, UserLogout
from resources.monitoramento_lote import MonitoramentoLote
from resources.requisicao import Requisicao
from blocklist import BLOCKLIST

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % config.PARAMS
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = config.SECRET_KEY
app.config['JWT_BLACKLIST_ENABLED'] = True

api = Api(app)
jwt = JWTManager(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

@jwt.token_in_blocklist_loader
def verifica_blocklist(self, token):
    return token['jti'] in BLOCKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidade():
    return jsonify({'message':'You have been logged out.'}), 401

api.add_resource(Upload, '/upload')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(Requisicao, '/requisicao/<string:service_ID>')
api.add_resource(MonitoramentoLote, '/monitoramento-lote')

if __name__=='__main__':
    from sql_alchemy import banco

    banco.init_app(app)
    app.run(debug=True)