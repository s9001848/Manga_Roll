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

        mangas = Manga.objects.create(name=name, author=author, manga_id=manga_id, category=category, description=description)
        mangas.save()
        alert = True
        return render(request, 'add_manga.html', { 'alert':alert })
    return render(request, 'add_manga.html')

