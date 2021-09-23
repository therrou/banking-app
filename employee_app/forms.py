
from django import forms

class CustomerFormCreateValidation(forms.Form):
    RANK_CHOICES = [
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('bronze', 'Bronze')
    ]

    username = forms.CharField(min_length=10, required=True)
    first_name = forms.CharField(min_length=5, required=True)
    last_name = forms.CharField(min_length=5, required=True)
    email = forms.CharField(min_length=10, required=True)
    customer_rank = forms.ChoiceField(choices=RANK_CHOICES)
    customer_phone_number = forms.CharField(min_length=10, required=True, max_length=20)
    customer_has_loan = forms.BooleanField(required=False, widget=forms.CheckboxInput)

    # class Meta:
    #     fields = '__all__'

class CustomerFormEditValidation(forms.Form):
    RANK_CHOICES = [
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('bronze', 'Bronze')
    ]

    id = forms.IntegerField(required=True)
    email = forms.CharField(min_length=10, required=True)
    customer_rank = forms.ChoiceField(choices=RANK_CHOICES)
    customer_phone_number = forms.CharField(min_length=10, required=True, max_length=20)
    customer_has_loan = forms.BooleanField(required=False, widget=forms.CheckboxInput)

class AccountFormCreateValidation(forms.Form):
    account_user_fk = forms.IntegerField(required=True)
    account_balance = forms.DecimalField(decimal_places=2, max_digits=7, required=True)