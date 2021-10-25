from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='post'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post'),
    path('like/<int:pk>', views.TooglePostLikeView.as_view(), name='post_like'),
]
