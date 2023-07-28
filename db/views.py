from django.shortcuts import render,redirect,get_object_or_404
from .forms import loginForm
from django.contrib.auth import authenticate,login
from django.contrib import messages


# def login_details(request):
#     # if request.method == 'POST':
#     #     form = loginForm()
#     #     if form.is_valid():
#     #         form.save()
#     #         return redirect('home')
#     # else:
#     #     form = loginForm()
#     #     return render(request,"login/index.html", {'form': form})

def login_details(request):
    if request.method == 'POST':
        form = loginForm()
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            #authentication
            user=authenticate(username=username,password=password)
            
            #check if user is valid
            if user is not None:
                login(request,user)
                messages.success(request, 'you have succesfuly logged in!')
                return redirect('home')
            else:
                messages.error(request, 'invalid username or password')
    else:
        form = loginForm()
        return render(request,"login/index.html", {'form': form})
