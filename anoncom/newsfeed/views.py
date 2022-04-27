from django.views import generic
from django.utils import timezone

from .models import News, Comments


class IndexView(generic.ListView):
    template_name = 'newsfeed/index.html'
    context_object_name = 'latest_news_list'

    def get_queryset(self):
        """
        Return the last ten published news (not including those set to be
        published in the future).
        """
        return News.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:10]


class DetailView(generic.DetailView):
    model = News
    template_name = 'newsfeed/detail.html'
