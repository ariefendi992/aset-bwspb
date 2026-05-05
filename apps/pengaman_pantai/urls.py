from django.urls import path
from . import views

app_name = "ppantai"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.create, name="create"),
    path("detail/<int:obj_id>/", views.detail, name="detail"),
    path("edit/<int:obj_id>/", views.update, name="edit"),
    path("delete/<int:obj_id>/", views.delete, name="delete"),
]
