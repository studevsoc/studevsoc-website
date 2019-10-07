from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.decorators import method_decorator
from datetime import date, datetime


from .models import Event
from .forms import EventForm, EventCategoryForm

def eventlist(request):
    today = date.today()
    current = datetime.today()
    upcomings = Event.objects.filter(date__gt=current, status=0).order_by('-date')
    pasts = Event.objects.filter(date__lt=today, status=0).order_by('-date')
    ongoing = Event.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day, status=0).order_by('-date')
    return render(request, 'events.html', {'upcomings':upcomings, 'pasts':pasts, 'ongoing':ongoing})
