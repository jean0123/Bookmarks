from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, mixins, response, serializers, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = UserSerializer
    search_fields = ('username',)
    filterset_fields = '__all__'
    permission_classes = [IsAdminUser]


class RolViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [IsAdminUser]


class BookmarkViewset(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Bookmark.objects.all()
        return Bookmark.objects.filter(created_by=user)


class BookmarkPublicViewset(viewsets.ModelViewSet):
    queryset = Bookmark.objects.filter(private=False).order_by('-id')
    serializer_class = BookmarkSerializer
    permission_classes = []
