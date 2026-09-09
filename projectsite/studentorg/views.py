from django.shortcuts import render
from .models import Organization


def organizations(request):
    organization_list = Organization.objects.all()

    return render(request, 'studentorg/organizations.html', {
        'organizations': organization_list
    })