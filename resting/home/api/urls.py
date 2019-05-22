from .views import posts, post_detail
from django.urls import path

app_name = "home"

urlpatterns = [
    path('', posts, name="posts"),  # /api/v1/posts/
    path('<int:id>', post_detail, name="posts")  # /api/v1/posts/id

]
