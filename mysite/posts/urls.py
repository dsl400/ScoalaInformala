from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.MyPostsView.as_view(), name='posts'),
    path('up/<int:post_id>', views.vote_up,name='vote_up'),
    path('down/<int:post_id>', views.vote_down,name='vote_down'),
    path('create_post', views.post, name='create_post'),
]