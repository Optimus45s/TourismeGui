from django.contrib import admin
from .models import Site, Hotel, Reservation, BlogPost

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type', 'latitude', 'longitude')
    list_filter = ('type',)
    search_fields = ('nom', 'type', 'description', 'historique')

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'adresse', 'prix_nuit', 'latitude', 'longitude', 'site_rel')
    list_filter = ('site_rel',)
    search_fields = ('nom', 'adresse', 'description')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'client', 'site', 'hotel', 'date_reservation', 'date_visite', 'nombre_personnes', 'status')
    list_filter = ('status', 'date_visite', 'site', 'hotel')
    search_fields = ('user__username', 'client', 'site__nom', 'hotel__nom')
    date_hierarchy = 'date_reservation'

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_publication')
    search_fields = ('titre', 'contenu')
    date_hierarchy = 'date_publication'
