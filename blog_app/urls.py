from django.urls import path
from blog_app import views

urlpatterns = [
    # path("", views.post_list, name='post-list'),
    path("", views.PostListView.as_view(), name='post-list'),
    
    # path("post-details/<int:pk>/", views.post_details, name='post-detail'),
    path("post-details/<int:pk>/", views.PostDetailView.as_view(), name='post-detail'),
    
    #  path("draft-list/", views.draft_list, name="draft-list"),
    path("draft-list/", views.DraftListView.as_view(), name="draft-list"),
        
    # path("draft-detail/<int:pk>/", views.draft_detail, name="draft-detail"),
    path("draft-detail/<int:pk>/", views.DraftDetailView.as_view(), name="draft-detail"),
        
    # path("draft-publish/<int:pk>/", views.draft_publish, name="draft-publish"),
    path("draft-publish/<int:pk>/", views.DraftPublishView.as_view(), name="draft-publish"),
        
    # path("post-delete/<int:pk>/", views.post_delete, name="post-delete"),
    path("post-delete/<int:pk>/", views.PostDeleteView.as_view(), name="post-delete"),
        
    # path("post-create/", views.post_create, name="post-create"),
    path("post-create/", views.PostCreateView.as_view(), name="post-create"),
        
    # path("post-update/<int:pk>/", views.post_update, name="post-update"),
    path("post-update/<int:pk>/", views.PostUpdateView.as_view(), name="post-update"),
       
]