from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserDetail, ParcelDelivery


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        # fields = ['username']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }


class SendParcel(forms.ModelForm):
    class Meta:
        model = ParcelDelivery
        fields = ['s_full_name', 's_number1', 's_number2', 's_address1', 's_address2',
                  's_city', 's_state', 's_zip', 's_country', 'r_full_name', 'r_number1', 'r_number2',
                  'r_address1', 'r_address2', 'r_city', 'r_state', 'r_zip', 'r_country']

        widgets = {
            's_full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
            's_number1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            's_address1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address line 1'}),
            's_address2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address line 2'}),
            's_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            's_state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            's_zip': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Zip or Postal code'}),
            'r_full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
            'r_number1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'r_address1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address line 1'}),
            'r_address2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address line 2'}),
            'r_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'r_state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'r_zip': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Zip or Postal code'}),
        }


class UserDetailsForm(forms.ModelForm):
    class Meta:
        fields = ['number1', 'number2']
        # fields = ['username','number1']

        model = UserDetail

        widgets = {
            'number1': forms.NumberInput(attrs={'class': 'form-control'}),
            'number2': forms.NumberInput(attrs={'class': 'form-control'}),
        }
