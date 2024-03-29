from django.urls import path
from blogapp import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/>', views.post_detail, name='post'),
    path('create_post/', views.create_post, name='create_post'),
    path('edit_post/<int:post_id>/>', views.edit, name='edit_post'),
    path('by_author/<author>/', views.posts_by_author, name='posts_by_author'),
    path('tags/<tag_slug>/', views.posts_by_tag, name='posts_by_tag')
]

