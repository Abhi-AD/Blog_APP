from django.urls import path
from blog_app import views

urlpatterns = [
    path("", views.post_list, name='post-list'),
    path("post-details/<int:pk>/", views.post_details, name='post-detail'),
    path("draft-list/", views.draft_list, name="draft-list"),
    path("draft-detail/<int:pk>/", views.draft_detail, name="draft-detail"),
    path("draft-publish/<int:pk>/", views.draft_publish, name="draft-publish"),
    path("post-delete/<int:pk>/", views.post_delete, name="post-delete"),
    path("post-create/", views.post_create, name="post-create"),
    path("post-update/<int:pk>/", views.post_update, name="post-update"),
]