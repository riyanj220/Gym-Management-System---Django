from django import forms
from .import models

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User 

class EnquiryForms(forms.ModelForm):
    class Meta:
        model = models.Enquiry

        fields = ('full_name','email','query')


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(), required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']


class EditUserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class EditUserPasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class TrainerLoginForm(forms.ModelForm):
    class Meta:
        model = models.Trainer
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }

class EditTrainerProfileForm(forms.ModelForm):
    class Meta:
        model = models.Trainer
        fields = ['full_name','mobile','address','details','img']


class EditTrainerPasswordForm(forms.Form):

    old_password = forms.CharField(
        max_length=50,required=True,
        widget=forms.PasswordInput(attrs={})
        )
    
    new_password1 = forms.CharField(
        max_length=50,required=True,
        widget=forms.PasswordInput(attrs={})
        )
    
    new_password2 = forms.CharField(
        max_length=50,required=True,
        widget=forms.PasswordInput(attrs={})
        )
    

class ReportToUserForm(forms.ModelForm):
    class Meta:
        model = models.TrainerSubscriberReport
        fields = ['receiver_user','report_msg','sender_trainer']
        widgets = {'sender_trainer':forms.HiddenInput()}


class ReportToTrainerForm(forms.ModelForm):
    class Meta:
        model = models.TrainerSubscriberReport
        fields = ['receiver_trainer','report_msg']
        widgets = {'sender_user':forms.HiddenInput()}