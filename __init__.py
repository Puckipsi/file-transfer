from flask import Flask


app = Flask(__name__, template_folder='application/templates')
app.config['UPLOAD_FOLDER']  = "files"

import application.routes
