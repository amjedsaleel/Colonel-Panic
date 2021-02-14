from django.shortcuts import render, redirect
from django.contrib import messages

# local Django
from . forms import CustomUserCreationForm
from startup.forms import CompanyForm

# Create your views here.


def register(request):
    register_form = CustomUserCreationForm()
    company_form = CompanyForm()

    context = {
        'register_form': register_form,
        'company_form': company_form
    }

    return render(request, 'accounts/register.html', context)


def register_individual(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            print('valid')
            form.save()
            messages.success(request, 'Account is successfully created')
            return redirect('accounts:register')

        messages.error(request, 'Error')
        return redirect('accounts:register')
