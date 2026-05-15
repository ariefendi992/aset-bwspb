from django.urls import include, path

urlpatterns = [
    path("danau/", include("apps.asets.urls.danau")),
    path("embung/", include("apps.asets.urls.embung")),
    path("bendung/", include("apps.asets.urls.bendung")),
    path("check-dam/", include("apps.asets.urls.checkdam")),
    path("pengaman-pantai/", include("apps.asets.urls.pantai")),
    path("tanggul-sungai/", include("apps.asets.urls.tanggul")),
    path("air-tanah/", include("apps.asets.urls.airtanah")),
    path("absah/", include("apps.asets.urls.absah")),
]
