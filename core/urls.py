from django.contrib import admin
from django.urls import path

from apps.dashboard.views import home

admin.site.site_header = "Centro de Inteligencia Calendario Blindado"
admin.site.site_title = "Calendario Blindado"
admin.site.index_title = "Panel de Monitoreo y Predicción"

urlpatterns = [
    path("", home, name="home"),
    path("centro-inteligencia/", admin.site.urls),
]
