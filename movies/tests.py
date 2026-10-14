from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Movie, Watchlist


class StreamHubTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='tester', password='testpassword123')
        self.movie = Movie.objects.create(
            title='Test Movie',
            description='A thrilling test movie synopsis.',
            category='movie',
            genre='Sci-Fi',
            release_year=2024,
            rating=8.9,
            duration='2h 10m',
            is_featured=True
        )
        self.series = Movie.objects.create(
            title='Test Series',
            description='A thrilling test series synopsis.',
            category='series',
            genre='Drama',
            release_year=2023,
            rating=9.1,
            duration='3 Seasons',
            is_featured=False
        )

    def test_homepage_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'StreamHub')
        self.assertContains(response, 'Welcome to Movie Streaming')
        self.assertContains(response, 'Test Movie')

    def test_form_html_url_compatibility(self):
        # Checks compatibility with the exact <a href="form.html"> link
        response = self.client.get('/form.html')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add to StreamHub')

    def test_login_html_url_compatibility(self):
        # Checks compatibility with the exact <a href="login.html"> link
        response = self.client.get('/login.html')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sign In')

    def test_movie_list_view(self):
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Movie')
        self.assertNotContains(response, 'Test Series')

    def test_series_list_view(self):
        response = self.client.get(reverse('series_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Series')
        self.assertNotContains(response, 'Test Movie')

    def test_movie_detail_view(self):
        response = self.client.get(reverse('movie_detail', args=[self.movie.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Movie')

    def test_add_movie_post(self):
        response = self.client.post(reverse('add_movie'), {
            'title': 'Brand New Cinema',
            'description': 'A newly posted film story.',
            'category': 'movie',
            'genre': 'Action',
            'release_year': 2025,
            'rating': 9.0,
            'duration': '1h 55m',
        })
        self.assertEqual(Movie.objects.filter(title='Brand New Cinema').count(), 1)

    def test_watchlist_toggle(self):
        self.client.login(username='tester', password='testpassword123')
        toggle_url = reverse('toggle_watchlist', args=[self.movie.pk])

        # Add to watchlist
        self.client.get(toggle_url)
        self.assertTrue(Watchlist.objects.filter(user=self.user, movie=self.movie).exists())

        # Remove from watchlist
        self.client.get(toggle_url)
        self.assertFalse(Watchlist.objects.filter(user=self.user, movie=self.movie).exists())

    def test_edit_movie_crud(self):
        edit_url = reverse('edit_movie', args=[self.movie.pk])
        response = self.client.post(edit_url, {
            'title': 'Test Movie Updated',
            'description': 'Updated story.',
            'category': 'movie',
            'genre': 'Thriller',
            'release_year': 2026,
            'rating': 9.5,
            'duration': '2h 15m',
        })
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, 'Test Movie Updated')
        self.assertEqual(float(self.movie.rating), 9.5)

    def test_delete_movie_crud(self):
        delete_url = reverse('delete_movie', args=[self.movie.pk])
        response = self.client.post(delete_url)
        self.assertFalse(Movie.objects.filter(pk=self.movie.pk).exists())

