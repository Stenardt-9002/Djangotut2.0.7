from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'Paypal')
)


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '2 nd street',
        'size' : "65",
    }))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Apartment or Bungalow',
        'size': "65",

    }))
    # country = CountryField(blank_label='(select country)').formfield(
    #     attrs = {
    #         'class': 'custom-select d-block w-100'
    #     }
    # )

    country = CountryField(blank_label='(Select Country)').formfield(
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100'
        })
    )

    zip = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    # same_billing_address = forms.BooleanField(widget=forms.CheckboxInput(required = False))
    same_shipping_address = forms.BooleanField(required=False)

    # save_info = forms.BooleanField(widget=forms.CheckboxInput(required = False))
    save_info = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)

    pass
