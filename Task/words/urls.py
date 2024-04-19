from django.urls import path

from .views import upload_file, table

app_name = "words"


urlpatterns = [
    path("upload_file/", upload_file, name="upload_file"),
    path("table/<file_name>/", table, name="table"),
]
