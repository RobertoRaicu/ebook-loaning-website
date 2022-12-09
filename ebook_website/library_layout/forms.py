from django import forms
from django.contrib.auth.models import User
from django.core import validators
from library_layout.models import review, ebook, author



# User forms
class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
    verify_pass = forms.CharField(widget=forms.PasswordInput())
    

    class Meta():
        model = User
        fields = ("username","password")

    def clean(self):
        all_clean_data = super().clean()
        password = all_clean_data['password']
        verify_pass = all_clean_data['verify_pass']

        if password != verify_pass:
            raise forms.ValidationError("passwords do not match")

class ReviewForm(forms.ModelForm):
    text_field = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',
                                                 'id':'message',
                                                 'placeholder':'Your review',
                                                 'required':'',}))
    class Meta():
        model = review
        fields = ("text_field",)

class EbookForm(forms.ModelForm):
    CHOICES = [
        ( 1, '14 days'),
        ( 2, '7 days'),
        ( 3, '3 days')
    ]
    loan_type = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES, 
    )
    ebook_content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',
                                                 'id':'message',
                                                 'placeholder':'text area',
                                                 'required':'false',
                                                 'style':'width: 80%',}))
    class Meta():
        model = ebook
        fields = '__all__'

class AuthorForm(forms.ModelForm):
    class Meta():
        model = author
        fields = '__all__'


    