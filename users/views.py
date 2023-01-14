from rest_framework.generics import ListAPIView, RetrieveAPIView, \
    DestroyAPIView, UpdateAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet

from users.models import User, Location
from users.serializers import UserListSerializer, UserDetailSerializer, \
    UserDestroySerializer, UserCreateSerializer, UserUpdateSerializer, \
    LocationSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer