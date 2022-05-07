from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Post, Post_anon, Comments, AnonComments
from .forms import CommentsForm, AnonCommentsForm


def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    # HTML template
    template_name = 'blog/home.html'
    # Change object name to loop over
    context_object_name = 'posts'
    # Ordering the posts according to date - newest first
    ordering = ['-date_posted']
    # Pagination
    paginate_by = 5


class PostAnonListView(ListView):
    model = Post_anon
    # HTML template
    template_name = 'blog/posts_anon_feed.html'
    # Change object name to loop over
    context_object_name = 'posts_anon'
    # Ordering the posts according to date - newest first
    ordering = ['-date_posted']
    # Pagination
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    # HTML template
    template_name = 'blog/user_posts.html'
    # Change object name to loop over
    context_object_name = 'posts'
    # Pagination
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    # Template post_detail.html
    model = Post
    form = CommentsForm

    def post(self, request, *args, **kwargs):
        form = CommentsForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            # return redirect('blog-home')
            return redirect(reverse('post-detail', kwargs={'pk': post.pk}))

    def get_success_url(self):
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        post_comments_count = Comments.objects.all().filter(post=self.object.id).count()
        post_comments = Comments.objects.all().filter(post=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })
        return context


class AnonPostDetailView(DetailView):
    # Template post_anon_detail.html
    model = Post_anon
    form = AnonCommentsForm

    def post(self, request, *args, **kwargs):
        form = AnonCommentsForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.post = post
            form.save()
            # return redirect('blog-home')
            return redirect(reverse('anon-post-detail', kwargs={'pk': post.pk}))

    def get_success_url(self):
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        post_comments_count = AnonComments.objects.all().filter(post=self.object.id).count()
        post_comments = AnonComments.objects.all().filter(post=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    # Template post_form.html
    model = Post
    fields = ['title', 'content']

    # Automatically setting user as author which is logged in
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostCreateAnonView(CreateView):
    # Template post_anon.html
    model = Post_anon
    fields = ['title', 'content']


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # Template post_update_form.html
    model = Post
    fields = ['title', 'content']
    template_name_suffix = '_update_form'

    # Automatically setting user as author which is logged in
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Tests if the user created the post in order to update it
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # Template post_confirm_delete.html
    model = Post
    success_url = '/'

    # Tests if the user created the post in order to update it
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
