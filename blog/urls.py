from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', views.blog_details, name='posts'),
    path('search-blog/', views.SearchBlogView.as_view(), name='searchblog'),
]
