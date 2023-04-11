from django.forms import ModelForm
from .models import Company, CompanyEmployer, User

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyEmployerForm(ModelForm):
    class Meta:
        model = CompanyEmployer
        fields = ['company', 'name', 'middleName']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

class PasswordForm(ModelForm):
    class Meta:
        model = User
        fields = ['password']