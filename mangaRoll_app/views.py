from django.shortcuts import redirect, render, HttpResponse
from .models import *
from .models import Manga
from .models import Chat
from .models import Manger
from .models import User
from . import forms, models
from datetime import date
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

# Add Manga
@login_required(login_url='/manger_login')
def add_manga(request):
    if request.method == 'POST':
        name = request.POST['name']
        author = request.POST['author']
        category = request.POST['category']
        description = request.POST['description']
        # pdf = request.FILES['pdfs']
        # image = request.FILES['images']

        mangas = Manga.objects.create(name=name, author=author, category=category, description=description)
        mangas.save()
        alert = True
        return render(request, 'add_manga.html', { 'alert':alert })
    return render(request, 'add_manga.html')

# View Manga
@login_required(login_url='/manger_login')
def view_mangas(request):
    mangas = Manga.objects.all()
    return render(request, 'view_mangas.html', { 'mangas':mangas })

# Profile Page
@login_required(login_url = '/manger_login')
def profile(request):
    return render(request, "profile.html")

# Edit Profile
@login_required(login_url = '/manger_login')
def edit_profile(request):
    users = Manger.objects.get(user=request.user)
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        profile_image = request.POST['profile_image']

        users.user.email = email
        users.name = name
        users.profile_image = profile_image
        users.user.save()
        users.save()
        alert = True
        return render(request, "edit_profile.html", {'alert':alert})
    return render(request, "edit_profile.html")

def delete_manga(request, myid):
    mangas = Manga.objects.filter(id=myid)
    mangas.delete()
    return redirect("/view_mangas")

def delete_user(request, myid):
    users = Manger.objects.filter(id=myid)
    users.delete()
    return redirect("/view_users")

def change_password(request):
    if request.method == "POST":
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(current_password):
                u.set_password(new_password)
                u.save()
                alert = True
                return render(request, "change_password.html", {'alert':alert})
            else:
                currpasswrong = True
                return render(request, "change_password.html", {'currpasswrong':currpasswrong})
        except:
            pass
    return render(request, "change_password.html")

def manger_registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        profile_image = request.FILES['profile_image']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        favorite_genre = request.POST['favorite_genre']

        if password != confirm_password:
            passnotmatch = True
            return render(request, "manger_registration.html", { 'passnotmatch': passnotmatch })

        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        manger = Manger.objects.create(user=user, profile_image=profile_image, favorite_genre=favorite_genre)
        user.save()
        manger.save()
        alert = True
        return render(request, "manger_login.html")
    return render(request, "manger_registration.html")

def manger_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponse('You are super user!')
            else:
                return redirect('profile')

        else:
            alert = True
            return render(request, 'manger_login.html', { 'alert': alert })
    return render(request, "manger_login.html")

def Logout(request):
    logout(request)
    return redirect ("/")