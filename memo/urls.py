from django.urls import path
from . import views

urlpatterns = [
    path('', views.memohome, name='memohome'),
    path('new', views.memonew, name='memonew'),
    path('create', views.memocreate, name='memocreate'),
    path('show/<int:memo_id>', views.memoshow, name='memoshow'),
    path('edit/<int:memo_id>', views.memoedit, name='memoedit'),
    path('update/<int:memo_id>', views.memoupdate, name='memoupdate'),
    path('delete/<int:memo_id>', views.memodelete, name='memodelete'),
    path('comentcreate/<int:memo_id>', views.comentcreate, name='comentcreate')
]