"""
URL configuration for tourismegui project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tourismegn import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('recherche/', views.recherche, name='recherche'),
    path('destinations/', views.destinations, name='destinations'),
    path('destination/<int:site_id>/', views.site_detail, name='site_detail'),
    path('reserver_hotel/<int:hotel_id>/', views.reserver_hotel, name='reserver_hotel'),
    path('reserver/', views.reserver, name='reserver'),
    path('reservation-success/', views.reservation_success, name='reservation_success'),
    path('reservation/', views.reserver_hotel, name='reservation'),
    path('inscription/', views.inscription, name='inscription'),
    path('mon_compte/', views.mon_compte, name='mon_compte'),
    path('listes_sites/', views.listes_sites, name='listes_sites'),
    path('confirmation_reservation/<int:reservation_id>/', views.confirmation_reservation, name='confirmation_reservation'),
    path('hotels/', views.hotels, name='hotels'),
    path('search/', views.search, name='search'),
    path('blog/', views.blog, name='blog'),
]
