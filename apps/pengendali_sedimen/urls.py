from django.urls import path
from . import views

app_name = "checkdam"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.create, name="create"),
    path("detail/<int:obj_id>/", views.detail, name="detail"),
    path("edit/<int:obj_id>/", views.update, name="edit"),
    path("delete/<int:obj_id>/", views.delete, name="delete"),
    path("download-foto/<int:foto_id>/", views.download_foto, name="download"),
    path("template/downlad", views.export_template, name="template"),
    path("template/import", views.import_template, name="import"),
]
