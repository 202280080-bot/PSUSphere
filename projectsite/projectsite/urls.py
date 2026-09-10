from django.contrib import admin
from django.urls import path, include
from home import views as home_views
from studentorg.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Homepage
    path('', HomePageView.as_view(), name='home'),

    # Existing pages
    path('announcements/', home_views.announcements, name='announcements'),
    path('', include('user_accounts.urls')),
    path('organizations/', include('studentorg.urls')),
]