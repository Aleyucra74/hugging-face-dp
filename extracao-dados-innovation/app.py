from flask import Flask
from flask_restful import Api
import pyodbc

import config
import main

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % config.PARAMS
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

if __name__=='__main__':
    from sql_alchemy import banco

    banco.init_app(app)
    app.run(debug=True)
    main.executar()