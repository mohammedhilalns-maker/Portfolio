from django import forms
from .models import *
from django import forms


class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields=['username','password']

class AboutForm(forms.ModelForm):
    class Meta:
        model=About
        fields=['about']

from django import forms
from .models import Addpersonaldetail

class PersonaldetailsForm(forms.ModelForm):
    class Meta:
        model = Addpersonaldetail
        fields = ['Nationality', 'State', 'District', 'DOB', 'Address', 'Religion', 'Sex']
        widgets = {
            'DOB': forms.DateInput(
                attrs={'type': 'date'}
            )
        }

class EducationalDetailsForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['University','Institute','CourseName','Duration','StartDate','EndDate']
        widgets = {
            'StartDate': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'EndDate': forms.DateInput(
                attrs={'type': 'date'}
            )
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['Company', 'Field', 'Status', 'Duration', 'StartDate', 'EndDate']
        widgets = {
            'StartDate': forms.DateInput(attrs={'type': 'date'}),
            'EndDate': forms.DateInput(attrs={'type': 'date'}),
        }

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Crtification
        fields =['Course','Defnition']

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields =['language']

class SkillForm(forms.ModelForm):
    class Meta:
        model = SKILL
        fields =['skill']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields=['FullName','Emailaddress','Subject','Message']