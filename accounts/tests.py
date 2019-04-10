#Testing Functionality of Registration Form

from django.test import TestCase
from .forms import UserRegistrationForm
from django import forms

# Create your tests here.


class CustomUserTest(TestCase):

    # Test to check that validation works when a user doesn't fill in at least one field
    def test_registration_form(self):
        form = UserRegistrationForm({
            'username': 'test',
            'email': 'test@example.com',
            'password1': 'example1',
            'password2': 'example1',
        })
        self.assertTrue(form.is_valid())


    # Test to check that validation works when a user doesn't provide a username and email
    def test_registration_form_fails_with_missing_email_and_username(self):
        form = UserRegistrationForm({
            'password1': 'example1',
            'password2': 'example1',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your email address",
                                 form.full_clean())


    # Test to check that validation works when a user's passwords don't match
    def test_registration_form_fails_wih_passwords_that_dont_match(self):
        form = UserRegistrationForm({
            'username': 'test',
            'email': 'test@example.com',
            'password1': 'example1',
            'password2': 'example2',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())


    # Test to check that validation works when a user doesn't fill in password1
    def test_registration_form_fails_with_empty_password1(self):
        form = UserRegistrationForm({
            'username': 'test',
            'email': 'test@example.com',
            'password2': 'example1',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Password must not be empty",
                                 form.full_clean())


    # Test to check that validation works when a user doesn't fill in password2
    def test_registration_form_fails_with_empty_password2(self):
        form = UserRegistrationForm({
            'username': 'test',
            'email': 'test@example.com',
            'password1': 'example1',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Password must not be empty",
                                 form.full_clean())