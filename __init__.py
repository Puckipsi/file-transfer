import os, os.path, time
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


@app.route('/view-uploads',methods=['GET'])
def uploaded_list():
	files = get_files()
	return render_template('display.html', files=files)


@app.route('/download/<file>', methods=["GET"])
def download(file):
    file_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'],file)
    return send_file(file_path, as_attachment=True)



def get_files():
	dir_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
	dir_files = os.listdir(dir_path)
	files = [{
		'file': file,
	    'upload_date':time.ctime(os.path.getctime(f"{dir_path}/{file}"))} for file in dir_files]  
	
	return files