from django import forms
from django.contrib.auth.models import User
from library_layout.models import UserProfileInfo
from django.core import validators


# User forms
class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
    verify_pass = forms.CharField(widget=forms.PasswordInput())
    

    class Meta():
        model = User
        fields = ("username","email","password")

    #validation error showing up only in terminal and not on page (HELP!!!)
    def IfUserExists(self,username):
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError(u'Username "%s" is already in use.' % username)

    def clean(self):
        all_clean_data = super().clean()
        password = all_clean_data['password']
        verify_pass = all_clean_data['verify_pass']

        if password != verify_pass:
            raise forms.ValidationError("passwords do not match")

    

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ("profile_pic",)

    