from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from .models import Organization


def organizations(request):
    organization_list = Organization.objects.all()
    return render(request, 'studentorg/organizations.html', {
        'organizations': organization_list
    })

def organization_detail(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    return render(request, 'studentorg/organization_detail.html', { 'organization': organization })


class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'
    paginate_by = 5