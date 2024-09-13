from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):

    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                msg = f'User {username} exists'
                messages.add_message(request, msg, extra_tags="error")
                return redirect('register')
            elif User.objects.filter(email=email).exists(): 
                msg = f'Email {email} is already registered'
                messages.info(request, msg, extra_tags="error")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=name)
                user.save()
                msg = f'User {username} created'
                messages.info(request, msg, extra_tags="message")
                return redirect('login')
        else:
            msg = 'Password not matching'
            messages.info(request, msg, extra_tags="error")
            return redirect('register')
    else:
        return render(request, 'register.html')
    

def login(request):
    if  request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            msg = 'Invalid credentials'
            messages.info(request, msg, extra_tags="error")
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')