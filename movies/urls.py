from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movie_list, name='movie_list'),
    path('series/', views.series_list, name='series_list'),
    path('watch/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('add/', views.add_movie, name='add_movie'),
    path('form.html', views.add_movie, name='form_html'),  # Direct compatibility with HTML snippet
    path('edit/<int:pk>/', views.edit_movie, name='edit_movie'),
    path('delete/<int:pk>/', views.delete_movie, name='delete_movie'),
    path('login/', views.login_view, name='login'),
    path('login.html', views.login_view, name='login_html'),  # Direct compatibility with HTML snippet
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('my-list/', views.my_list, name='my_list'),
    path('watchlist/toggle/<int:pk>/', views.toggle_watchlist, name='toggle_watchlist'),
]
