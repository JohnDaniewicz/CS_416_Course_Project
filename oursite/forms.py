from django import forms
from .models import Register


class RegisterForm(forms.Form):
    first_name = forms.CharField(required=True,  max_length=60)
    last_name = forms.CharField(required=True, max_length=60)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['first_name', 'last_name', 'email', 'message']