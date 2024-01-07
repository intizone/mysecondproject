from django.urls import path
from myapp.views import *

app_name = 'yourapp'

urlpatterns = [
    path("", home, name="home"),

    # Categories
    path("categories/view/", view_category, name="view_category"),
    path("categories/update/", update_category, name="update_category"),
    path("categories/delete/", delete_category, name="delete_category"),
    path("categories/create/", create_category, name="create_category"),

    # Teams
    path("teams/view/", view_teams, name="view_teams"),
    path("teams/update/", update_team, name="update_team"),
    path("teams/delete/", delete_team, name="delete_team"),
    path("teams/create/", create_team, name="create_team"),

    # Reservations
    path("reservations/view/", view_reservations, name="view_reservations"),
    path("reservations/update/", update_reservation, name="update_reservation"),
    path("reservations/delete/", delete_reservation, name="delete_reservation"),
    path("reservations/create/", create_reservation, name="create_reservation"),
]
