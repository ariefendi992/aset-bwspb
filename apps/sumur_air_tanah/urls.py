from django.urls import path
from . import views

app_name = "sumur"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.create, name="create"),
    path("detail/<int:id>/", views.detail, name="detail"),
    path("edit/<int:id>/", views.update, name="edit"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path(r"unduh/template-excel/", views.export_template, name="template"),
    path(r"import/template-excel/", views.import_excel, name="import"),
]
