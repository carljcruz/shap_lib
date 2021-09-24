from django.shortcuts import redirect, render
from django.http import HttpResponse
from accounts.forms import EmployeeForm
from accounts.admin import UserCreationForm
from django.contrib.auth import get_user_model, login

User = get_user_model()

def home_view(request):
    return render(request, 'home.html', context=None)



def create_user(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        employee_form = EmployeeForm(request.POST)
        if user_form.is_valid() and employee_form.is_valid():
            user = user_form.save()
            employee = employee_form.save(commit=False)
            employee.user = user
            employee.save()
            login(request, user)
            return redirect('home')
    else:
        user_form = UserCreationForm()
        employee_form = EmployeeForm()
    context = {
        'user_form': user_form,
        'employee_form': employee_form
    }
    
    return render(request,'emp_signup.html',context=context)






