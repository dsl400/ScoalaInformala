from django.shortcuts import render
from posts.forms import NewPostForm
from posts.models import Post
from django.views.generic import  ListView
from django.views.generic import TemplateView


class HomePageView(ListView):
    model = Post
    template_name = 'homepage.html'
    paginate_by = 5

    def get_queryset(self):        
        return Post.objects.filter(votes__gt=-10).order_by('-id')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = NewPostForm
        return context

class AboutPageView(TemplateView):
    template_name = 'about.html'