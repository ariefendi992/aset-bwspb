from django.urls import path
from apps.asets.views.airtanah import *

app_name = "sumur"
urlpatterns = [
    path("", index, name="index"),
    path("add/", create, name="create"),
    path("detail/<int:id>/", detail, name="detail"),
    path("edit/<int:id>/", update, name="edit"),
    path("delete/<int:id>/", delete, name="delete"),
    path(r"unduh/template-excel/", export_template, name="template"),
    path(r"import/template-excel/", import_excel, name="import"),
]
