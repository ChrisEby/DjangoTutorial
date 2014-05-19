from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_blog_posts'

    def get_queryset(self):
        """
        TODO: Return back the latest blog posts
        """
        return HttpResponse("Index")


class DetailView(generic.DetailView):
    #model = Question
    template_name = 'blog/detail.html'

    def get_queryset(self):
        """
        TODO: Excludes any blog posts that aren't published yet.
        """
        #return Question.objects.filter(pub_date__lte=timezone.now())
        return HttpResponse("Detail")
