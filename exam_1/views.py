from django.shortcuts import render,redirect
from .models import Author,Books,Orders


def home(request):
    authors = Author.objects.all()
    return render(request, 'home.html', {'authors': authors})


def create_author(request):
    if request.method == 'POST':
        name_author = request.POST.get('name_author')
        Author.objects.create(name_author=name_author)
        return redirect('home')
    return render(request, 'author.html')



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


def create_book(request):
    authors = Author.objects.all()
    if request.method == 'POST':
        author = Author.objects.get(id=request.POST.get('author'))
        book_name = request.POST.get('book_name')
        title = request.POST.get('title')
        caption = request.POST.get('caption')
        Books.objects.create(author=author,book_name=book_name,title=title,caption=caption)
        return redirect('home')
    return render(request,'book.html',{'authors':authors})


def update_book(request,id):
    book = Books.objects.get(id=id)
    authors = Author.objects.all()
    if request.method == 'POST':
        book.author = Author.objects.get(id=request.POST.get('author'))
        book.book_name = request.POST.get('book_name')
        book.title = request.POST.get('title')
        book.caption = request.POST.get('caption')
        book.save()
        return redirect('home')
    return render(request,'book.html',{'book':book,'authors':authors})


def delete_book(request,id):
    book = Books.objects.get(id=id)
    book.delete()
    return redirect('home')