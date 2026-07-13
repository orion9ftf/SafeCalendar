from django.urls import path

from .views import event_detail, home

urlpatterns = [
    path("", home, name="home"),

    path(
        "evento/<uuid:event_id>/",
        event_detail,
        name="event_detail"
    ),
]
