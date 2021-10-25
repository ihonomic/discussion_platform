from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='post'),
    path('like/<int:pk>', views.LikeAPostView.as_view(), name='post_like'),
]
