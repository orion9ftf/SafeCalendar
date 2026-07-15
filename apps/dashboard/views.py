from django.shortcuts import get_object_or_404, render

from apps.events.models import Event


def home(request):
    events = Event.objects.filter(
        is_active=True
    ).order_by("event_date")

    calendar_events = []

    for event in events:
        calendar_events.append({
            "title": event.name,
            "start": str(event.event_date),
            "url": f"/evento/{event.id}/",
        })

    return render(
        request,
        "dashboard/home.html",
        {
            "events": events,
            "calendar_events": calendar_events
        }
    )


def event_detail(request, event_id):
    event = get_object_or_404(
        Event,
        id=event_id,
        is_active=True
    )

    if event.risk_level == "CRITICAL":
        a, b, c = -1.6, 0, 160

    elif event.risk_level == "HIGH":
        a, b, c = -1.2, 0, 120

    elif event.risk_level == "MEDIUM":
        a, b, c = -0.8, 0, 80

    else:
        a, b, c = -0.5, 0, 50

    points = []

    for x in range(-10, 11):
        y = (a * (x ** 2)) + (b * x) + c

        if y < 0:
            y = 0

        points.append({
            "x": x,
            "y": round(y, 2)
        })

    return render(
        request,
        "dashboard/event_detail.html",
        {
            "event": event,
            "points": points
        }
    )
