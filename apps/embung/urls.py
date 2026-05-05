from django.urls import path
from . import views

app_name = "embung"

urlpatterns = [
    path(r"", views.index_embung, name="index"),
    path("add-data/", views.add_embung, name="add"),
    path("detail-data/<int:id>  ", views.detail_embung, name="detail"),
    path("edit-data/<int:id>  ", views.update_embung, name="edit"),
    path("delete-data/<int:id>  ", views.delete_embung, name="delete"),
    path(r"unduh/template-excel/", views.export_template, name="template"),
    path(r"import/template-excel/", views.import_excel, name="import"),
]
