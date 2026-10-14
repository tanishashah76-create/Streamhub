from django.contrib import admin
from .models import Movie, Watchlist


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'genre', 'release_year', 'rating', 'is_featured', 'created_at')
    list_filter = ('category', 'genre', 'is_featured', 'release_year')
    search_fields = ('title', 'description')
    list_editable = ('rating', 'is_featured')


@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'added_at')
    list_filter = ('added_at',)
    search_fields = ('user__username', 'movie__title')
