from django.shortcuts import render
from .models import Announcement


def home(request):
    return render(request, 'home/index.html')


def announcements(request):
    announcement_list = Announcement.objects.all()

    return render(request, 'home/announcements.html', {
        'announcements': announcement_list
    })