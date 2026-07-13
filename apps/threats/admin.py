from django.contrib import admin

from .models import Threat


@admin.register(Threat)
class ThreatAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owasp_category",
        "risk_level",
        "is_active",
    )

    search_fields = (
        "name",
        "owasp_category",
    )

    list_filter = (
        "risk_level",
        "is_active",
    )
    