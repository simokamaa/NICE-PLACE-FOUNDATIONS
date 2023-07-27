from django import forms
from .models import login_details

class loginForm():
    class Meta:
        model = login_details
        
        fields=['username','password']
        