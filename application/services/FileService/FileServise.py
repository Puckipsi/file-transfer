import os
from __init__ import app
from flask import request, render_template, send_file
from config import get_current_datetime
from utils.timing import timing


class FileService:

    def __init__(self, FileManager):
        self.file_maneger = FileManager()


    def start_page(self):
        return render_template("upload.html")


    def upload(self):
        file_attributes, duration =  self.get_uploading_attributes()
      
        if not file_attributes: 
            return "You forget to choose file. Return and choose file"
        
        full_path, filename, datetime = file_attributes

        return render_template(
                "download.html", file=full_path, filename=filename, datetime=datetime, duration=duration
        )
         
    
    @timing 
    def get_uploading_attributes(self):
        file = request.files["file"]
        filename = file.filename
        
        if filename:

            file.save("/".join((self.get_upload_folder(), filename)))
            datetime = get_current_datetime()
            full_path = f"{request.url_root}download/{filename}"

            return full_path, filename, datetime   
    

    def download(self, file):
        file_path = self.file_maneger.get_file_path(self.get_upload_folder(), file)
        return send_file(file_path, as_attachment=True)
    
    
    def remove(self, file):
        file_path = self.file_maneger.get_file_path(self.get_upload_folder(), file)

        try:
            os.remove(file_path)
        except Exception as e:
            print("An error occurred while removing file", e)
        finally:
            return self.view_uploads()


    def view_uploads(self):
        files = self.file_maneger.load_uploaded_files(self.get_upload_folder())
        return render_template("display.html", files=files)


    @staticmethod
    def get_upload_folder():
        return app.config["UPLOAD_FOLDER"]
