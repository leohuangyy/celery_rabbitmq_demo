# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts
# Create your views here.
def users_list(request):
    users=User.objects.all()
    return render(request,'user_list.html',{'users':users})



def generate_random_user(request):
    if request.method == 'POST':
	form = GenerateRandomUserForm(request.POST)
	if form.is_valid():
	    total = form.cleaned_data.get('total')
	    create_random_user_accounts.delay(total)
	    messages.success(request,'We are generating your random users!Wait a moment and refresh this page.')
	    return redirect('users_list')
    else:
        form = GenerateRandomUserForm()
    return render(request,'generate_random_user.html',{'form':form})


