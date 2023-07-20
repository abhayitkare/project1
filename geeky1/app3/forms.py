from django import forms

# create Registration Form using UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class formsp(UserCreationForm):
    password2 = forms.CharField(label='confirm password (again)',widget=forms.PasswordInput)  # all ready ahe mhanun ethe validation lava lagat ahe
    class Meta:
        model = User             # in-build model use kel 
        fields = ['username','first_name','last_name','email']  # ya extra fields add karnya sathi apan asa code lihila
        labels = {'email':'Email'}


