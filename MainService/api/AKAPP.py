from flask import Flask

from config import *
 
from flask_cors import CORS
from flasgger import Swagger, swag_from


app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'AKEmailServices API',
    'uiversion': 3
}
Swagger(app, template=Swagger_template)



# from flask_api import FlaskAPI
# app = FlaskAPI(__name__)
CORS(app)

app.debug = True

app.config['SECRET_KEY'] = AK_API_JWT_SECRET_KEY
app.config['JWT_ALGORITHM'] = AK_JWT_ALGORITHM
app.config['JWT_VERIFY_CLAIMS']   = [] #['signature', 'nbf', 'iat'] # 'exp',
app.config['JWT_REQUIRED_CLAIMS'] = [] #[ 'iat', 'nbf']  # 'exp',
