"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# from django_countries.fields import CountryField
from datetime import date
from .models import *
from django.forms import extras

BIRTH_YEAR_CHOICES = [(date.today().year-i) for i in range(120)]

class UserForm(forms.ModelForm) :
    email = forms.EmailField(help_text="Please enter your email.")
    first_name = forms.CharField(help_text="Please enter your first name.")
    last_name = forms.CharField(help_text="Please enter your last name.")
    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta :
        model = User
        fields = ('first_name','last_name','email') 

class UserProfileForm(forms.ModelForm) :
    #username = forms.CharField(widget=forms.HiddenInput())
    dob = forms.DateField(widget=forms.extras.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    # country = CountryField()
    class Meta :
        model = AppUserprofile
        fields = (
		'dob',
		'mobile_no',
		'education_place',
		'education_field',
		'employment_place',
		'employment_designation',
		'occupation',
		'residence_place',
		'country',
		'picture'
		)

    def clean_mobile_no(self): 
        mobile_no = self.cleaned_data.get('mobile_no')
        if not( len(mobile_no) == 10 ):
            raise forms.ValidationError("Enter valid mobile number!")
        return mobile_no


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = (
			'pt_id',
			'text',
			'likes',
			'up',
			'time'
			)

# class ProfileForm(forms.ModelForm) :
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput())
#     class Meta :
#         model = UserProfile
#         exclude = ('aadhar_card_no','gender','first_name','psswd')

#     def clean_mobile_no(self): 
#         mobile_no = self.cleaned_data.get('mobile_no')
#         if not( len(mobile_no) == 10 ):
#             raise forms.ValidationError("Enter valid mobile number!")
#         return mobile_no
