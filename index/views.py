from django.shortcuts import render,redirect
from about .models import *
from contact .models import *
from home .models import *
from portfolios .models import *
from resume .models import *
from about .urls import *

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, admin_only



from django.contrib import messages

def index(request):
    total=Home.objects.all()
    about=About.objects.all()
    service=Service.objects.all()
    client=Client.objects.all()
    fact=Facts.objects.all()
    profile=Profile.objects.all()
    resume=resume_study.objects.all()
    work=work_history.objects.all()
    skill=Skill.objects.all()
    technical=Technical.objects.all()
    folio=portfolio.objects.all()
    catfolio=Category.objects.all()
    contact=Contact.objects.all()
    context={
        'about':about,
        'total':total,
        'service':service,
        'client':client,
        'fact':fact,
        'profile':profile,
        'resume':resume,
        'work':work,
        'skill':skill,
        'technical':technical,
        'folio':folio,
        'contact':contact,
        'catfolio':catfolio,
    }
    return render(request, "Frontend/layout/layout.py",context)

@admin_only
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('addintro')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account is successfully created for ' + user)

                return redirect('login')

        context = {'form':form}
        return render(request, 'register/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('addintro')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('addintro')
            else:
                messages.info(request, 'Username and Password Does not Match')

        context = {}
        return render(request, 'login/login.html', context)
    
def logoutUser(request):
	logout(request)
	return redirect('login')


