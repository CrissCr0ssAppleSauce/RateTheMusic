from django.urls import path
from . import views
urlpatterns = [
	path('', views.index),
	path('Artist/<str:pk>/', views.artist_index),
	path('Artist/<str:pk>/Chat/<str:room_name>/', views.room, name='room'),
	path('Artist/<str:pk1>/Album/<str:pk2>', views.album_index),
]
