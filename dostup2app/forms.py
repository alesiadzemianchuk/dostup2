from .models import Order
from django.forms import ModelForm, CheckboxInput, Select, DateInput, DateTimeInput, CheckboxSelectMultiple
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, EmailInput


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['department', 'employee', 'date_created', 'Телефонная_связь', 'Электронная_почта']
        widgets = {
            'department': Select(attrs={
                'class': 'form-control custom-select',

                'placeholder': 'Выберите отдел'

            }),
            'employee': Select(attrs={
                'class': 'form-control custom-select',
                'placeholder': 'Выберите ФИО'

            }),
            'date_created': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD'
            }),
            'Телефонная_связь': CheckboxInput(attrs={
                'class': 'custom-control custom-checkbox'
            }),
            'Электронная_почта': CheckboxInput(attrs={
                'class': 'custom-control custom-checkbox'

            })
        }


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
        widgets = {
            'username': TextInput(
                attrs={
                    'name': 'name',
                    'id': 'name',
                    'placeholder': 'Username'
                }
            ),
            'password1': PasswordInput(
                attrs={
                    'name': 'pass',
                    'id': 'pass',
                    'placeholder': 'Password'
                }
            ),
            'password2': PasswordInput(
                attrs={
                    'name': 're-pass',
                    'id': 're-pass',
                    'placeholder': 'Password'
                }
            ),
            'email': EmailInput(
                attrs={
                    'name': 'email',
                    'id': 'email',
                    'placeholder': 'Email'
                }

            )
        }