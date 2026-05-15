from django.urls import path
from apps.asets.views.danau import *

app_name = "danau"
urlpatterns = [
    path(r"", index_danau, name="index"),
    path(r"detail/<int:id>/", detail_danau, name="detail"),
    path(r"add-data/", add_danau, name="add_danau"),
    path(r"edit-data/<int:id>/", update_danau, name="edit"),
    path(r"delete-data/<int:id>/", delete_danau, name="delete"),
    path(r"template-excel", export_template_excel, name="template"),
    path("upload-template/", import_excel, name="import"),
]
