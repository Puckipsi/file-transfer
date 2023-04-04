from __init__ import app
from application.services.FileService.FileServise import FileService
from application.services.FileService.FileManager import FileManager


file_service = FileService(FileManager)

app.add_url_rule(
    rule="/", methods=["GET"], view_func=file_service.start_page)

app.add_url_rule(
    rule="/upload", methods=["POST"], view_func=file_service.upload)

app.add_url_rule(
    rule="/download/<file>", methods=["GET"], view_func=file_service.download)

app.add_url_rule(
    rule="/view-uploads", methods=["GET"], view_func=file_service.view_uploads)


app.add_url_rule(
    rule="/remove/<file>", methods=["GET"], view_func=file_service.remove)

