from django.urls import path
from apps.asets.views.tanggul import *

app_name = "tsungai"
urlpatterns = [
    path("", index, name="index"),
    path("add/", create, name="create"),
    path("detail/<int:id>/", detail, name="detail"),
    path("edit/<int:id>/", update, name="edit"),
    path("delete/<int:id>/", delete, name="delete"),
    path("download-foto/<int:id>/", donwload, name="download"),
    path("template/downlad", export_template, name="template"),
    path("template/import", import_template, name="import"),
]
