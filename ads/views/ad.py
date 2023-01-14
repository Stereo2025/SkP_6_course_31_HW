from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.generic import ListView
from rest_framework.generics import RetrieveAPIView, CreateAPIView, \
    UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad
from ads.permissions import AdUpdatePermission
from ads.serializers import AdImageSerializer, AdSerializer, \
    AdUpdateSerializer, AdCreateSerializer


class AdListView(ListView):
    models = Ad
    queryset = Ad.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        categories = request.GET.getlist('cat', None)
        if categories:
            self.object_list = self.object_list.filter(
                category_id__in=categories)

        if request.GET.get('price_form', None):
            self.object_list = self.object_list.filter(
                price__gte=request.GET.get("price_from"))
        if request.GET.get('price_to', None):
            self.object_list = self.object_list.filter(
                price__lte=request.GET.get("price_to"))
        if request.GET.get('text', None):
            self.object_list = self.object_list.filter(
                name__icontains=request.GET.get("text"))
        if request.GET.get('location', None):
            self.object_list = self.object_list.filter(
                author__locations__name__icontains=request.GET.get("location"))

        self.object_list = self.object_list.select_related('author').order_by(
            "-price")
        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        ads = []
        for ad in page_obj:
            ads.append({
                "id": ad.id,
                "name": ad.name,
                "author_id": ad.author_id,
                "author": ad.author.first_name,
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "category_id": ad.category_id,
                "image": ad.image.url if ad.image else None,
            })

        response = {
            "items": ads,
            "num_pages": page_obj.paginator.num_pages,
            "total": page_obj.paginator.count,
        }

        return JsonResponse(response, safe=False)


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer
    permission_classes = [IsAuthenticated, AdUpdatePermission]


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer
    permission_classes = [IsAuthenticated, AdUpdatePermission]


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, AdUpdatePermission]


class AdImageView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdImageSerializer
