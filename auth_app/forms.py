from django.contrib.auth.forms import UserCreationForm
# Equivalent: from django.forms import ModelForm
from django import forms
from .models import Profile

# SignupUserForm inherits from UserCreationForm
class SignupUserForm(UserCreationForm):
    # As UserCreationForm provides only 3 params 
    # username, password1, password2 we create the others
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=100, required=True)

    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2',
    ]


class SignupProfileForm(forms.ModelForm):
    # The Meta class has two functions:
    # 1. Indicate which model we are using
    # 2. Show the fields we want to include in our final form
    class Meta:
        model = Profile

        # Customizing label for mfe
        labels = {
            'customer_mfe': 'Multi-factor auth enabled'
        }

        fields = [
            'customer_phone_number',
            'customer_mfe'
        ]

class LoginForm(forms.Form):
    # LoginForm has to be without model otherwise it takes validations
    # from the user model which implies that is_valid() will fail

    username = forms.CharField(label="Write your username", max_length=100)
    password = forms.CharField(label="Password", max_length=100)

    fields = [
        'username',
        'password'
    ]