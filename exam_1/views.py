from django.shortcuts import render,redirect
from .models import Author,Books,Orders

# Create your views here.

def create_author(request):
    if request.method == 'POST':
        name_author = request.POST.get('name')
        title = request.POST.get('title')
        return redirect('home.html')
    



def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        caption = request.POST.get('caption')


def create_order(request):
    if request.method == 'POST':
        name_customer = request.POST.get('name_customer')
        name_author = request.POST.get('name_author')
        book_name = request.POST.get('book_name')


def delete_author(request):
    pass