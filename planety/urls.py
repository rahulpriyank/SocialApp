from django.urls import path
from . import views
from . views import UserPostListView, PostDetailView, PostDeleteview, PostCreateView, PostUpdateView,CommentUpdateView, VideoCreateView, video_update

urlpatterns = [
    path('',views.base, name='base'),
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('index',views.index, name='index'),
    path('logout',views.logout, name='logout'),
    path('like_post', views.like_post, name='like_post'),
    path('find_friends',views.find_friends, name='find_friends'),
    path('profile',views.profile, name='profile'),

    path('profile_update', views.profile_update, name='profile_update'),
    path('user/<str:username>', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post_details' ),
    
    path('profile_posts',views.profile_posts, name='profile_posts'),
    path('post/new/',PostCreateView.as_view(), name='post-create' ),
    path('post_update',views.post_update, name='post_update'),
    path('post/<int:pk>/update',PostUpdateView.as_view(), name='post-update' ),
    path('profile_photos',views.profile_photos, name='profile_photos'),
]

