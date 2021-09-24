from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.models import ModelForm

from accounts.models import Employee, MyUser

class EmployeeForm(ModelForm):

    class Meta:
        model = Employee
        fields = ('department',)