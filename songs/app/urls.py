from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
   # path('',views.index, name='index'),
   
    path('',views.song_list, name='song_list'),
    path('add/', views.add_song, name='add_song'),
    path('delete/<int:pk>/', views.delete_song, name='delete'),
    path('update/<int:pk>/', views.update_view, name='update'),
    path('update_song/', views.update_song, name='update_song'),
    path('play/<int:pk>/', views.play_song, name='play'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)