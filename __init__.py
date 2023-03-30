from flask import Flask, render_template, request
from config import get_current_datetime


app = Flask(__name__)


   
@app.route('/')
def index():
	return render_template("upload.html")

@app.route('/upload',  methods=['POST'])
def upload():
	file = request.files['file']
	filename = file.filename
	file.save(filename)
	datetime = get_current_datetime()
	file_path = f'{request.remote_addr}{app.root_path}/files/{filename}'
	
	return {"datetime": datetime, "file_path": file_path}