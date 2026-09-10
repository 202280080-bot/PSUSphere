from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Organization


def organizations(request):
    organization_list = Organization.objects.all()
    return render(request, 'studentorg/organizations.html', {
        'organizations': organization_list
    })


class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'
    paginate_by = 5