from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import F
from posts.models import Post, Vote
from users.forms import UserImageForm
from .forms import NewPostForm
from django.http import  HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import  ListView

@login_required(login_url='/users/login')
def post(request):
    if request.method == 'GET':
        form = NewPostForm()
        return render(request,'post.html',{'form':form})
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.creator = request.user
            post.save()
        return redirect(reverse('posts:posts'))

class MyPostsView(ListView):
    model = Post
    template_name = 'my_posts.html'
    paginate_by = 5

    # @login_required()
    @method_decorator(login_required(login_url='/users/login'))
    def dispatch(self, request, *args, **kwargs):
        return super(MyPostsView,self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Post.objects.filter(votes__gt=-10,creator=self.request.user).order_by('-id')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = NewPostForm
        return context

@login_required(login_url='/users/login')
def vote_up(request,post_id):
    old_vote = 0
    try:
        old_vote = Vote.objects.get(user=request.user,post_id=post_id).vote
    except ObjectDoesNotExist:
        pass
    if old_vote < 1:
        Vote.objects.update_or_create(user=request.user,post_id=post_id,defaults={
            'vote': old_vote + 1
        })
        Post.objects.filter(pk=post_id).update(votes=F("votes")+1)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url='/users/login')
def vote_down(request,post_id):
    old_vote = 0
    try:
        old_vote = Vote.objects.get(user=request.user,post_id=post_id).vote
    except ObjectDoesNotExist:
        pass
    if old_vote > -1:
        Vote.objects.update_or_create(user=request.user,post_id=post_id,defaults={
            'vote': old_vote - 1
        })
        Post.objects.filter(pk=post_id).update(votes=F("votes")-1)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

