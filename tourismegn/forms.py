from django import forms
from tourismegn.models import Reservation

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['site', 'hotel', 'date_visite', 'nombre_personnes']
        widgets = {
            'date_visite': forms.DateInput(attrs={'type': 'date'}),
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'client', 'site', 'hotel', 'date_reservation', 'date_visite', 'nombre_personnes', 'status']  



class RechercheForm(forms.Form):
    recherche = forms.CharField(max_length=255, required=False)
    type_site = forms.ChoiceField(choices=[('nature', 'Nature'), ('culture', 'Culture')], required=False)
