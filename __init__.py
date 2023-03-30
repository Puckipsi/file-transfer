import os
from flask import Flask, render_template, request, send_file
from config import get_current_datetime


app = Flask(__name__)
app.config['UPLOAD_FOLDER']  = "files"


   
@app.route('/')
def index():
	return render_template("upload.html")

@app.route('/upload',  methods=['POST'])
def upload():
	file = request.files['file']
	filename = file.filename
	file.save('/'.join((app.config['UPLOAD_FOLDER'],filename)))
	datetime = get_current_datetime()
	full_path = f'{request.url_root}download/{filename}'

	return render_template('download.html', file=full_path, filename=filename, datetime=datetime)


@app.route('/download/<file>', methods=["GET"])
def download(file):
    file_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'],file)
    return send_file(file_path, as_attachment=True)
