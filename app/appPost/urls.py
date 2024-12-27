from django.urls import path

from .views import CreatePostView, create_post, get_posts


app_name = 'appPost'

urlpatterns = [
    path('', get_posts, name="menu"), 
    path('postear/', CreatePostView.as_view(), name='postear')

]

