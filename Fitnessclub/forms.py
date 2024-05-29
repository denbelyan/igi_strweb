from django import forms
from .models import Client, Card, Service, Hall, Employee, News, WorkVakansiya, feedback
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import EmailValidator, RegexValidator



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))


def clean(self):
    self.check_email(self.cleaned_data.get('email'))
    self.check_passwords(self.cleaned_data.get('password1'), self.cleaned_data.get('password2'))
    self.check_password_length(self.cleaned_data.get('password1'))
    self.check_age(self.cleaned_data.get('age'))
    self.check_telephone(self.cleaned_data.get('telephone'))



class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    }))


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('name', 'hall', 'price', 'start_work', 'end_work')

    price = forms.IntegerField(min_value=0,widget=forms.NumberInput(attrs={}))


class ClientForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={}), validators=[EmailValidator()])
    phone = forms.CharField(widget=forms.TextInput(attrs={}), validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number.')])

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'address', 'phone']

class Employeeform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name','last_name')
class Hallform(forms.ModelForm):
    class Meta:
        model = Hall
        fields = ('name', 'price_per_night', 'schedule')

    price_per_night = forms.IntegerField(min_value=0,widget=forms.NumberInput(attrs={}))

class ImageFormNews(forms.ModelForm):
    class Meta:
        model = News
        fields = ['image']

class WorkForm(forms.ModelForm):
    class meta:
        model = WorkVakansiya
        fields =('name', 'salary')

class feedbackForm(forms.ModelForm):
    class meta:
        model = feedback
        fields = ('text', 'stars', 'author')

    stars = forms.IntegerField(min_value=0,widget=forms.NumberInput(attrs={}))

