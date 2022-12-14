from django.shortcuts import redirect, render, HttpResponse
from .models import *
from . import forms, models
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

# Add Manga
@login_required(login_url='/user_login')
def add_manga(request):
    if request.method == 'POST':
        name = request.POST['name']
        author = request.POST['author']
        manga_id = request.POST['manga_id']
        category = request.POST['category']
        description = request.POST['description']
        pdf = request.FILES['pdfs']
        image = request.FILES['images']

        mangas = Manga.objects.create(name=name, author=author, manga_id=manga_id, category=category, description=description, pdf=pdf, image=image)
        mangas.save()
        alert = True
        return render(request, 'add_manga.html', { 'alert':alert })
    return render(request, 'add_manga.html')

# View Manga
@login_required(login_url='/user_login')
def view_mangas(request):
    mangas = Manga.objects.all()
    return render(request, 'view_mangas.html', { 'mangas':mangas })

# Profile Page
@login_required(login_url = '/user_login')
def profile(request):
    return render(request, "profile.html")

# Edit Profile
@login_required(login_url = '/user_login')
def edit_profile(request):
    users = users.objects.get(user=request.user)
    if request.method == "POST":
        name = request.POST['name']
        author = request.POST['author']
        manga_id = request.POST['manga_id']
        category = request.POST['category']
        description = request.POST['description']
        pdf = request.FILES['pdfs']
        image = request.FILES['images']

        users.user.name = name
        users.author = author
        users.manga_id = manga_id
        users.category = category
        users.description = description
        users.pdf = pdf
        users.image = image
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
    users = User.objects.filter(id=myid)
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
