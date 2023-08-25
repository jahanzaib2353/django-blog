from . import views
from .views import show_all_posts
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('all-posts/', views.show_all_posts, name='all_posts'),  # Moved this line above the post_detail pattern
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # ... other URL patterns ...
]
