from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from rest_framework.generics import ListCreateAPIView


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]    
    serializer_class = SongSerializer

    def get_queryset(self):
        return Song.objects.filter(album_id=self.kwargs.get("pk"))

    def perform_create(self, serializer):        
        return serializer.save(album_id=self.kwargs.get("pk"))
