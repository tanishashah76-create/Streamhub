from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    CATEGORY_CHOICES = [
        ('movie', 'Movie'),
        ('series', 'Series'),
    ]

    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Drama', 'Drama'),
        ('Comedy', 'Comedy'),
        ('Thriller', 'Thriller'),
        ('Horror', 'Horror'),
        ('Romance', 'Romance'),
        ('Adventure', 'Adventure'),
        ('Animation', 'Animation'),
        ('Fantasy', 'Fantasy'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='movie')
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, default='Action')
    release_year = models.PositiveIntegerField(default=2024)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=8.5)
    duration = models.CharField(max_length=50, default='2h 15m')
    poster_url = models.URLField(max_length=600, blank=True, null=True)
    backdrop_url = models.URLField(max_length=600, blank=True, null=True)
    video_url = models.URLField(max_length=600, blank=True, null=True, help_text="YouTube embed or video URL")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.release_year})"

    @property
    def get_poster_url(self):
        if self.poster_url:
            return self.poster_url
        return "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=600&q=80"


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlist')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='watchlisted_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')
        ordering = ['-added_at']

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"
