from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def registration(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            
            return redirect('home')
        else:
            return render(request, 'registration.html', {'form':form})
    else:
        print('get request')
    return render(request, 'registration.html', {})
    