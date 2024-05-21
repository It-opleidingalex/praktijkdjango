from django.shortcuts import render
from .models import Event

def home(request):
    events = Event.objects.all().order_by('start_time')
    return render(request, 'agenda/home.html', {'events': events})

def event_list(request):
    events = Event.objects.all().order_by('start_time')
    return render(request, 'agenda/event_list.html', {'events': events})
