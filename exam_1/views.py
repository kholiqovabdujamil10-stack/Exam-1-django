from django.shortcuts import render,redirect
from .models import Author,Books,Orders

def create_author(request):
    if request.method == 'POST':
        name_author = request.POST.get('name_author')
        Author.objects.create(name_author=name_author)
        return redirect('home')
    return render(request, 'author.html')


def home(request):
    authors = Author.objects.all()
    return render(request, 'home.html', {'authors': authors})


def update_author(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        name_author = request.POST.get('name_author')
        author.name_author = name_author
        author.save()
        return redirect('home')
    return render(request, 'author.html', {'author': author})


def delete_author(request, id):
    author = Author.objects.get(id=id)
    author.delete()
    return redirect('home')