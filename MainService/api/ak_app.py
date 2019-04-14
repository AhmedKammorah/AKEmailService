from flask import Flask

from MainService.api.config import *
 
from flask_cors import CORS
from flasgger import Swagger, swag_from


app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'AKEmailServices API',
    'uiversion': 3,
    'host':DOCS_HOST
}
Swagger(app, template_file='swagger/docs_swagger.yml')

CORS(app)

app.debug = True

app.config['SECRET_KEY'] = AK_API_JWT_SECRET_KEY
app.config['JWT_ALGORITHM'] = AK_JWT_ALGORITHM
app.config['JWT_VERIFY_CLAIMS']   = [] 
app.config['JWT_REQUIRED_CLAIMS'] = []
app.config['JWT_HEADER_TYPE'] = 'Bearer'
app.config['JWT_AUTH_HEADER_PREFIX'] = 'Bearer'
# app.config['JWT_AUTH_URL_RULE'] ='/api/auth'