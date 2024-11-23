from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from tourismegn.models import Hotel, Site, Reservation
from tourismegn.forms import ReservationForm, RechercheForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm

from django.shortcuts import render

def reservation_success(request):
    return render(request, 'reservation_success.html')


@login_required
def reserver(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservation_success')
    else:
        form = ReservationForm()

    return render(request, 'reserver.html', {'form': form})

def home(request):
    sites = Site.objects.all()[:3]
    hotels = Hotel.objects.all()[:3]
    return render(request, 'tourismegn/home.html', {'sites': sites, 'hotels': hotels})

from django.contrib import messages

def destinations(request):
    type_site = request.GET.get('type_site', None)
    
    if type_site:
        sites = Site.objects.filter(type=type_site)
        if not sites.exists():
            messages.info(request, f"Aucun site trouvé pour le type '{type_site}'.")
    else:
        sites = Site.objects.all()
    
    return render(request, 'destinations.html', {'sites': sites})


def hotels(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels.html', {'hotels': hotels})

def search(request):
    query = request.GET.get('q', '')
    hotels = Hotel.objects.filter(nom__icontains=query)  
    sites = Site.objects.filter(nom__icontains=query) 
    return render(request, 'search.html', {'hotels': hotels, 'sites': sites, 'query': query})

def blog(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})


def site_detail(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    hotels = Hotel.objects.filter(adresse__icontains=site.nom)  
    return render(request, 'site_detail.html', {'site': site, 'hotels': hotels})

def recherche(request):
    form = RechercheForm(request.GET)
    sites = Site.objects.all()
    hotels = Hotel.objects.all()

    if form.is_valid():
        recherche = form.cleaned_data.get('recherche')
        type_site = form.cleaned_data.get('type_site')

        if recherche:
            sites = sites.filter(nom__icontains=recherche)
            hotels = hotels.filter(nom__icontains=recherche)
        if type_site:
            sites = sites.filter(type=type_site)

    return render(request, 'recherche.html', {'form': form, 'sites': sites, 'hotels': hotels})

def reserver_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)

    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.utilisateur = request.user  
            reservation.save()  
            return redirect('confirmation_reservation', reservation.id)
    else:
        form = ReservationForm(initial={'hotel': hotel})

    return render(request, 'reservation.html', {'form': form, 'hotel': hotel})

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm

def inscription(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('mon_compte')
    else:
        form = UserRegisterForm()

    return render(request, 'registration/inscription.html', {'form': form})


@login_required
def mon_compte(request):
    return render(request, 'registration/mon_compte.html')

def listes_sites(request):
    sites = Site.objects.all()
    return render(request, 'tourismegn/listes_sites.html', {'sites': sites})

def confirmation_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    return render(request, 'confirmation_reservation.html', {'reservation': reservation})
