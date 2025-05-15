from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.tweet_list, name='tweet_list'),
    # path('tweet_list/', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.delete_tweet, name='delete_tweet'),
]
