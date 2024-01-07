from django.contrib import admin
from django.urls import path, include 
from myapp.views import home,create_category, create_team, create_reservation, delete_category, delete_team, delete_reservation, home, update_category, update_team, update_reservation, view_category, view_reservations, view_teams
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("", include('myapp.urls')),  # Include the URLs from 'myapp'
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
