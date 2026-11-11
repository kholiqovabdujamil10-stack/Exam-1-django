from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('create_author/', create_author, name='create_author'),
    path('update_author/<int:id>/', update_author, name='update_author'),
    path('delete_author/<int:id>/', delete_author, name='delete_author'),
]