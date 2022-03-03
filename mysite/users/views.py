import imp
from random import randint
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, Http404, reverse
from users.forms import LoginForm, ProfileImageForm, UserForm, RegisterForm, UserImageForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from posts.models import Post
from django.db import IntegrityError

# Create your views here.
def register(request):
    if request.method == 'GET':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email.split('@')[0]
            try:
                user.save()
            except IntegrityError:
                messages.error(request,'nume utilizator existent')
                return render(request, 'users/register.html', {
                    'form': form,
                })

            return redirect('/')

    return render(request, 'users/register.html', {
        'form': form,
    })

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'GET':
        form = LoginForm()
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            raise Http404('Username or password not provided!')
        from urllib.parse import urlparse, parse_qs
        url = urlparse(request.META.get('HTTP_REFERER', '/'))
        query = parse_qs(url.query)
        redirect_url = query.get('next',['/posts'])[0]
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request,'nume utilizator sau parola incorecta')
        else:
            login(request, user)
            return redirect(redirect_url)


    return render(request, 'users/login.html', {'form': form, 'error':error})


def logout_user(request):
    logout(request)
    max_posts = Post.objects.count()
    post = Post.objects.get(pk=randint(1, max_posts))
    print(post)
    return render(request,'users/logout.html',{'post':post})



@login_required(login_url='/users/login')
def upload_view(request):
    if request.method == 'POST':
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            f_name = form.save(request.user.id)
            Profile.objects.update_or_create(user_id=request.user.id,defaults={
                'avatar': f_name
            })
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url='/users/login')
def profile_view(request):
   
    # print(profile_form)
    if request.method == 'GET':
        profile_form = UserForm(initial={
            'first_name':request.user.first_name,
            'last_name':request.user.last_name,
            'username':request.user.username,
            'email':request.user.email
        })
        # print(profile_form)
        form = ProfileImageForm()     
    else:
        form = ProfileImageForm()
        
        if form.is_valid():
           
            form.save()
            return redirect(reverse('users:profile'))

    return render(request, 'users/profile.html', {
        'form': form,
        'profile_form':profile_form
    })

@login_required(login_url='/users/login')
def profile_update(request):
    profile_form = UserForm()
    if request.method == 'GET':
        form = ProfileImageForm()
    else:
        profile_update_form = UserForm(request.POST, instance=request.user)
        if profile_update_form.is_valid():
            profile_update_form.save()          
            return redirect(reverse('users:profile'))

    return render(request, 'users/profile.html', {
        'form': form,
        'profile_form':profile_form
    })


