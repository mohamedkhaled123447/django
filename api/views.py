from rest_framework import generics
from .models import Gallery, Message,Video
from .serializers import GallerySerializer, MessageSerializer,VideoSerializer

# Gallery Views


class GalleryListCreateView(generics.ListCreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

    def get_queryset(self):
        gallery_type = self.request.query_params.get("type")
        queryset = Gallery.objects.all()

        if gallery_type:
            queryset = queryset.filter(type=gallery_type)

        return queryset


class GalleryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


# Message Views


class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
class VideoListCreateView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
