from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post

# Create your views here.

class IndexView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super(HomePageView, self).get_context_data(**kwargs)
		context['latest_post'] = Post.objects.all()[:1]
		return context

