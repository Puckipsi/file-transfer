import os
import time
from __init__ import app


class FileManager:

    def load_uploaded_files(self, upload_folder):
        dir_path = os.path.join(app.root_path, upload_folder)
        dir_files = os.listdir(dir_path)
        files = [{
		    'file': file,
            "size": os.path.getsize(f"{dir_path}/{file}"),
	        'upload_date': time.ctime(os.path.getctime(f"{dir_path}/{file}"))} for file in sorted(dir_files)]  
        
        return files
    

    def get_file_path(self, folder_name, file):
        file_path = os.path.join(app.root_path, folder_name, file)
        return file_path
    
    