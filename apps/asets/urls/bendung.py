from django.urls import path
from apps.asets.views.bendung import *

app_name = "bendung"
urlpatterns = [
    path("", index_bendung, name="index"),
    path("add-data/", add_bendung, name="add"),
    path("edit-data/<int:id>/", update_bendung, name="edit"),
    path("download-foto/<int:foto_id>/", download_foto, name="download_foto"),
    path(r"delete-data/<int:id>/", delete_data, name="delete"),
    path(r"detail-data/<int:id>/", detail_bendung, name="detail"),
    path(r"template/download/", export_template, name="template"),
    path(r"template/import-excel/", import_excel, name="import"),
]
