from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post
from files.models import File

# Create your views here.

class IndexView(TemplateView):
    template_name = "base_home.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['latest_post'] = Post.objects.latest('created')
        context['latest_files'] = File.objects.order_by('-last_download')[:10]
        context['popular_files'] = File.objects.order_by('-download_count')[:10]
        return context

