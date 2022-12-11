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