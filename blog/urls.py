from django.urls import path
from . import views


urlpatterns = [
    path('<slug:category_slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name="post_single"),
    path('<slug:category_slug>/', views.PostListView.as_view(), name="post_list"),
    path('', views.HomeView.as_view(), name="home"),
]
