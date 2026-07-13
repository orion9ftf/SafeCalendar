from django.shortcuts import get_object_or_404, render

from apps.events.models import Event

def home(request):
    events = Event.objects.filter(
        is_active=True
    ).order_by("event_date")

    return render(
        request,
        "dashboard/home.html",
        {
            "events": events
        }
    )


def event_detail(request, event_id):
    event = get_object_or_404(
        Event,
        id=event_id,
        is_active=True
    )

    return render(
        request,
        "dashboard/event_detail.html",
        {
            "event": event
        }
    )
