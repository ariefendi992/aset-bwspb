from django.urls import path
from . import views

app_name = "tsungai"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.create, name="create"),
    path("detail/<int:id>/", views.detail, name="detail"),
    path("edit/<int:id>/", views.update, name="update"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path("download-foto/<int:id>/", views.donwload, name="download"),
]
