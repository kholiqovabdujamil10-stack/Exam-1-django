from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('create_author/', create_author, name='create_author'),
    path('update_author/<int:id>/', update_author, name='update_author'),
    path('delete_author/<int:id>/', delete_author, name='delete_author'),

    path('create_book/',create_book, name='create_book'),
    path('update_book/<int:id>/',update_book, name='update_book'),
    path('delete_book/<int:id>/',delete_book, name='delete_book'),

    path('create_order/',create_order,name='create_order'),
    path('update_order/<int:id>/',update_order,name='update_order'),
    path('delete_order/<int:id>/',delete_order,name='delete_order'),
]