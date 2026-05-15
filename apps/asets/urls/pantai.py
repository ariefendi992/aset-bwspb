from django.urls import path
from apps.asets.views.pantai import *

app_name = "ppantai"
urlpatterns = [
    path("", index, name="index"),
    path("add/", create, name="create"),
    path("detail/<int:obj_id>/", detail, name="detail"),
    path("edit/<int:obj_id>/", update, name="edit"),
    path("delete/<int:obj_id>/", delete, name="delete"),
    path("template/downlad", export_template, name="template"),
    path("template/import", import_template, name="import"),
]
