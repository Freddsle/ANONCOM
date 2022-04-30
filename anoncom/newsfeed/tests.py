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
        AllPost.objects.create(post_title='just a test', post_text='a', post_author='admin', pub_date='2021-04-27')

    def test_text_content(self):
        post = AllPost.objects.get(id=1)
        expected_object_name = f'{post.post_title}'
        self.assertEqual(expected_object_name, 'just a test')
    
    def test_post_detail_view(self):
        response = self.client.get('/1/')
        no_response = self.client.get('/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'newsfeed/post_detail.html')
    
    def test_post_create_view(self):
        response = self.client.post(reverse('newsfeed:post_new'), {
            'post_title': 'New title',
            'post_text': 'New text',
            #'author': self.user,
            })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')
    
    def test_post_update_view(self): # new
        response = self.client.post(reverse('post_edit', args='1'), {
        'title': 'Updated title',
        'body': 'Updated text',
        })
        self.assertEqual(response.status_code, 302)
    
    def test_post_delete_view(self): # new
        response = self.client.get(
        reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 200)
