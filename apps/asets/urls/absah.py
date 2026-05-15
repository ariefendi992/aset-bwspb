from django.urls import path
from apps.asets.views.absah import *

app_name = "absah"
urlpatterns = [
    path("", index, name="index"),
    path("add/", create, name="create"),
    path("edit/<int:id>/", update, name="edit"),
    path("detail/<int:id>/", detail, name="detail"),
    path("delete/<int:id>/", delete, name="delete"),
    path("download-file/<int:id>/", download_foto, name="download"),
    path("template/download", export_template, name="template"),
    path("template/import", import_template, name="import"),
]
