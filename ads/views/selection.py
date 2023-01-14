from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ads.models import Selection
from ads.permissions import SelectionUpdatePermission
from ads.serializers import SelectionSerializer, SelectionCreateSerializer, \
    SelectionUpdateSerializer


class SelectionListView(generics.ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class SelectionDetailView(generics.RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class SelectionCreateView(generics.CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateSerializer
    permission_classes = [IsAuthenticated]


class SelectionUpdateView(generics.UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionUpdateSerializer
    permission_classes = [IsAuthenticated, SelectionUpdatePermission]


class SelectionDeleteView(generics.DestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated, SelectionUpdatePermission]
