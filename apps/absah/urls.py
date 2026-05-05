from django.urls import path
from . import views

app_name = "absah"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.create, name="create"),
    path("edit/<int:id>/", views.update, name="update"),
    path("detail/<int:id>/", views.detail, name="detail"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path("download-file/<int:id>/", views.download_foto, name="download"),
]
