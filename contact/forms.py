from django import forms
from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Full name *', widget=forms.TextInput({'placeholder': 'Enter your full name'}), required=True)
    contact_email = forms.EmailField(label='Email *', widget=forms.TextInput({'placeholder': 'Enter your email'}), required=True)
    phone_number = PhoneNumberField(error_messages={'invalid': 'Phone number must be 10 or 11 digits.'}, 
                   widget=forms.TextInput({'placeholder': 'Enter your number'}), required=False)
    message = forms.CharField(label='Your enquiry *', widget=forms.Textarea({'placeholder': 'Enter your message'}), required=True)