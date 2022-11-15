from django import forms
from django.contrib.auth.models import User
from library_layout.models import UserProfileInfo

# User forms
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = "__all__"

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = "__all__"