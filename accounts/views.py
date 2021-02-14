from django.shortcuts import render, redirect
from django.contrib import messages, auth

# local Django
from . models import CustomUser

# Create your views here.


def login(request):
    if request.method == 'POST':
        print('ok')
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are logged in')
            return redirect('startup:home')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('accounts:login')

    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:

            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'user name is already exists')
                return redirect('accounts:register')

            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Email is already exists, please chose another one')
                return redirect('accounts:register')

            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            user.save()
            messages.success(request, 'Account created Successfully')
            return redirect('accounts:login')

        else:
            context = {'username': username, 'email': email}
            messages.error(request, 'Password do not match')
            return render(request, 'accounts/signup.html', context)

    return render(request, 'accounts/signup.html')


