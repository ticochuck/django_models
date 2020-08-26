from django.urls import include, path

from .views import HomePage, PostDetailPage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('post_detail/<int:pk>', PostDetailPage.as_view(), name='post_detail'),
]
