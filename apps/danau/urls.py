from django.urls import path
from . import views

app_name = "danau"
urlpatterns = [
    path(r"", views.index_danau, name="index"),
    path(r"detail/<int:id>/", views.detail_danau, name="detail"),
    path(r"add-data/", views.add_danau, name="add_danau"),
    path(r"edit-data/<int:id>/", views.update_danau, name="edit"),
    path(r"delete-data/<int:id>/", views.delete_danau, name="delete"),
    path(r"template-excel", views.export_template_excel, name="template"),
    path("upload-template/", views.import_excel, name="import"),
]
