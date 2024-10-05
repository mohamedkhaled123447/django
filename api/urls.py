from django.urls import path
from .views import (
    GalleryListCreateView,
    GalleryRetrieveUpdateDeleteView,
    MessageListCreateView,
    MessageRetrieveUpdateDeleteView,
    VideoListCreateView,
    VideoRetrieveUpdateDeleteView,
)

urlpatterns = [
    path("gallery/", GalleryListCreateView.as_view(), name="gallery-list-create"),
    path(
        "gallery/<int:pk>/",
        GalleryRetrieveUpdateDeleteView.as_view(),
        name="gallery-detail",
    ),
    path("message/", MessageListCreateView.as_view(), name="message-list-create"),
    path(
        "message/<int:pk>/",
        MessageRetrieveUpdateDeleteView.as_view(),
        name="message-detail",
    ),
    path("video/", VideoListCreateView.as_view(), name="video-list-create"),
    path(
        "video/<int:pk>/",
        VideoRetrieveUpdateDeleteView.as_view(),
        name="video-detail",
    ),
]
