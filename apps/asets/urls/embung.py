from django.urls import path
from apps.asets.views.embung import *

app_name = "embung"

urlpatterns = [
    path(r"", index_embung, name="index"),
    path("add-data/", add_embung, name="add"),
    path("detail-data/<int:id>  ", detail_embung, name="detail"),
    path("edit-data/<int:id>  ", update_embung, name="edit"),
    path("delete-data/<int:id>  ", delete_embung, name="delete"),
    path(r"unduh/template-excel/", export_template, name="template"),
    path(r"import/template-excel/", import_excel, name="import"),
]
