from django.views import generic
from django.utils import timezone
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy

from .models import AllPost, Comment


class IndexView(generic.ListView):
    template_name = 'newsfeed/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """
        Return the last ten published news (not including those set to be
        published in the future).
        """
        return AllPost.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]


class DetailView(generic.DetailView):
    model = AllPost
    template_name = 'newsfeed/detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = AllPost
    template_name = 'newsfeed/post_new.html'
    context_object_name = 'post'
    fields = ['post_title', 'post_text']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.post_author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.edit.UpdateView):
    model = AllPost
    template_name = 'newsfeed/post_edit.html'
    context_object_name = 'post'
    fields = ['post_title', 'post_text']
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.post_author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.edit.DeleteView):
    model = AllPost
    template_name = 'newsfeed/post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('newsfeed:index')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.post_author == self.request.user
