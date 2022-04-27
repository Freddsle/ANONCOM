from django.test import TestCase
from django.urls import reverse

from .models import AllPost


class AllPostIndexViewTests(TestCase):

    def test_no_post(self):
        """
        If no posts exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('newsfeed:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts are available.")
        self.assertQuerysetEqual(response.context['latest_post_list'], [])


class PostModelTest(TestCase):

    def setUp(self):
        AllPost.objects.create(post_title='just a test', post_text='a', post_author='a', pub_date='2021-04-27')

    def test_text_content(self):
        post = AllPost.objects.get(id=1)
        expected_object_name = f'{post.post_title}'
        self.assertEqual(expected_object_name, 'just a test')
    