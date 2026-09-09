from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('announcements/', views.announcements, name='announcements'),
    path('', include('user_accounts.urls')),
    path('organizations/', include('studentorg.urls')),
]