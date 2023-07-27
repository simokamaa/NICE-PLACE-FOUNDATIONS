from django.shortcuts import render,redirect,get_object_or_404
from .forms import loginForm
from django.contrib.auth import authenticate,login


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
    form = loginForm()
    return render(request,"login/index.html", {'form': form})
