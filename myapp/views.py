from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import FoodCategory, Team, Reservalition



# views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import FoodCategory, Team, Reservalition

def home(request):
    return render(request, "index.html")

def view_category(request):
    try:
        categories = FoodCategory.objects.all()
        response_content = ""
        for category in categories:
            response_content += f"Category: {category.name}, {category.icon}\n"
        return HttpResponse(response_content)
    except FoodCategory.DoesNotExist:
        return HttpResponse("No categories found")
def view_teams(request):
    try:
        teams = Team.objects.all()
        response_content = ""
        for team in teams:
            response_content += f"Team: {team.name}, {team.position}, {team.img}\n"
        return HttpResponse(response_content)
    except Team.DoesNotExist:
        return HttpResponse("No teams found")

def view_reservations(request):
    try:
        reservations = Reservalition.objects.all()
        response_content = ""
        for reservation in reservations:
            response_content += f"Reservation: {reservation.name}, {reservation.phone}, {reservation.reservedDate}, {reservation.reservatiuonTime}, {reservation.comments}\n"
        return HttpResponse(response_content)
    except Reservalition.DoesNotExist:
        return HttpResponse("No reservations found")

def update_category(request):
    try:
        category = FoodCategory.objects.get(id=1)
        category.name = 'Updated Name'
        category.icon = 'updated_icon.jpg'
        category.save()
        return HttpResponse("Category updated successfully")
    except FoodCategory.DoesNotExist:
        raise Http404("Category does not exist")

def update_reservation(request):
    try:
        reservation = Reservalition.objects.get(id=1)
        reservation.name = 'Updated Name'
        reservation.phone = 'Updated Phone'
        reservation.reservedDate = '01.01.01'
        reservation.reservatiuonTime = '02:02'
        reservation.comments = 'Updated Comments'
        reservation.save()
        return HttpResponse("Reservation updated successfully")
    except Reservalition.DoesNotExist:
        raise Http404("Reservation does not exist")

def update_team(request):
    try:
        team = Team.objects.get(id=1)
        team.name = 'Updated Team Name'
        team.position = 'Updated Position'
        team.img = 'updated_image.jpg'
        team.about = 'Updated About'
        team.save()
        return HttpResponse("Team updated successfully")
    except Team.DoesNotExist:
        raise Http404("Team does not exist")
    
def delete_category(request):
    try:
        category = FoodCategory.objects.get(id=2)
        category.delete()
        return HttpResponse("Category deleted successfully")
    except FoodCategory.DoesNotExist:
        raise Http404("Category does not exist")
    
def delete_reservation(request):
    try:
        reservation = Reservalition.objects.get(id=2)
        reservation.delete()
        return HttpResponse("Reservation deleted successfully")
    except Reservalition.DoesNotExist:
        raise Http404("Reservation does not exist")

def delete_team(request):
    try:
        team = Team.objects.get(id=2)
        team.delete()
        return HttpResponse("Team deleted successfully")
    except Team.DoesNotExist:
        raise Http404("Team does not exist")

def create_category(request):
    category = FoodCategory.objects.create(
        name = "birinchi category",
        icon = "image.jpg"
    )
    return HttpResponse("Category created successfully")

def create_reservation(request):
    reservation = Reservalition.objects.create(
        name = "Zoirbek To'xtasinov",
        phone = "+998998888888",
        reservedDate = "2021-09-15",
        reservatiuonTime = "15:00:00",
        comments = "qisqacha tafsilot"
    )
    return HttpResponse("Reservation created successfully")

def create_team(request):
    team = Team.objects.create(
        name = "Zoirbek To'xtasinov",
        position = "Backend Developer",
        img = "image.jpg",
        about = "qisqacha tafsilot"
    )
    return HttpResponse("Team member created successfully")

# def get_category(request):
#     category = get_object_or_404(FoodCategory, id=1)
#     return HttpResponse(f"Category: {category.name}, {category.icon}")
# def get_reservation(request):
#     reservation = get_object_or_404(Reservalition, id=1)
#     return HttpResponse(f"Reservation: {reservation.name}, {reservation.phone}, {reservation.reservedDate}, {reservation.reservatiuonTime}, {reservation.comments}")
# def get_team(request):
#     team = get_object_or_404(Team, id=1)
#     return HttpResponse(f"Team: {team.name}, {team.position}, {team.img}, {team.about}")
# def get_category_by_name(request):
#     category = get_object_or_404(FoodCategory, name="birinchi category")
#     return HttpResponse(f"Category: {category.name}, {category.icon}")
# def get_reservation_by_name(request):
#     reservation = get_object_or_404(Reservalition, name="Zoirbek To'xtasinov")
#     return HttpResponse(f"Reservation: {reservation.name}, {reservation.phone}, {reservation.reservedDate}, {reservation.reservatiuonTime}, {reservation.comments}")
# def get_team_by_name(request):
#     team = get_object_or_404(Team, name="Zoirbek To'xtasinov")
#     return HttpResponse(f"Team: {team.name}, {team.position}, {team.img}, {team.about}")
