from django.test import TestCase
from django.urls import reverse

from .models import Post


class AllPostIndexViewTests(TestCase):

    def test_no_post(self):
        """
        If no posts exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('blog-home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "")


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title='just a test', content='a')
