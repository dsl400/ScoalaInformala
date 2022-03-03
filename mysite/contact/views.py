from random import randint
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from contact.forms import ContactForm
from posts.models import Post

# Create your views here.


class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm
        return context

    def post(self,request):
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            return redirect('/contact/thanks')

def thanks(request):
    max_posts = Post.objects.count()
    post = Post.objects.get(pk=randint(1, max_posts))
    return render(request,'thanks.html',{'post':post})