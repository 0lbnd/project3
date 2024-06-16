from django.test import TestCase
from rest_framework.test import APIClient
from .models import Post, Comment

class PostModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Test Post", content="Test Content")

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.post = Post.objects.create(title="Test Post", content="Test Content")

    def test_get_posts(self):
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, 200)
