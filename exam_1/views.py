from django.shortcuts import render,redirect
from .models import Author,Books,Orders


def home(request):
    authors = Author.objects.all()
    books = Books.objects.all()
    orders = Orders.objects.all()
    return render(request,'home.html',{'authors':authors,'books':books,'orders':orders})

# ==== Author ==== 

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

# ==== Books ====

def create_book(request):
    authors = Author.objects.all()
    if request.method == 'POST':
        author = Author.objects.get(id=request.POST.get('author'))
        book_name = request.POST.get('book_name')
        title = request.POST.get('title')
        caption = request.POST.get('caption')
        picture = request.FILES.get('picture')
        Books.objects.create(author=author,book_name=book_name,title=title,caption=caption, picture=picture)
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
        picture = request.FILES.get('picture')
        if picture:
            book.picture = picture
        book.save()
        return redirect('home')
    return render(request,'book.html',{'book':book,'authors':authors})


def delete_book(request,id):
    book = Books.objects.get(id=id)
    book.delete()
    return redirect('home')

# ==== Orders ====

def create_order(request):
    books = Books.objects.all()
    if request.method == 'POST':
        name_customer = request.POST.get('name_customer')
        time_taken = request.POST.get('time_taken')
        time_bring = request.POST.get('time_bring')
        order = Orders.objects.create(name_customer=name_customer,time_taken=time_taken,time_bring=time_bring)
        order.book_name.set(request.POST.getlist('book_name'))
        return redirect('home')
    return render(request,'order.html',{'books':books})


def update_order(request,id):
    order = Orders.objects.get(id=id)
    books = Books.objects.all()
    if request.method == 'POST':
        order.name_customer = request.POST.get('name_customer')
        order.time_taken = request.POST.get('time_taken')
        order.time_bring = request.POST.get('time_bring')
        order.save()
        order.book_name.set(request.POST.getlist('book_name'))
        return redirect('home')
    return render(request,'order.html',{'order':order,'books':books})



def delete_order(request,id):
    order = Orders.objects.get(id=id)
    order.delete()
    return redirect('home')