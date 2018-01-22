from django.urls import path

from . import views

app_name='songs'
urlpatterns = [
    path('', views.song_list, name='list'),
    path('song<int:song_pk>/', views.song_detail, name='detail'),
    path('performer<int:performer_pk>/', views.performer_detail, name='performer'),
]
