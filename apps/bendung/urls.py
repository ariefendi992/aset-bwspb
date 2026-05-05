from django.urls import path
from . import views

app_name = "bendung"
urlpatterns = [
    path("", views.index_bendung, name="index"),
    path("add-data/", views.add_bendung, name="add"),
    path("edit-data/<int:id>/", views.update_bendung, name="edit"),
    path("download-foto/<int:foto_id>/", views.download_foto, name="download_foto"),
    path(r"delete-data/<int:id>/", views.delete_data, name="delete"),
    path(r"detail-data/<int:id>/", views.detail_bendung, name="detail"),
    path(r"template/download/", views.export_template, name="template"),
]
