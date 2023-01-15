from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.relations import SlugRelatedField

from ads.models import Ad, Selection, Category
from users.models import User


class NotTrueValidator:
    def __call__(self, value):
        if value:
            raise serializers.ValidationError("Новое объявление не может быть опубликовано")


class AdSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Ad
        fields = '__all__'


class AdListSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username',
                              queryset=User.objects.all())
    category = SlugRelatedField(slug_field='name',
                                queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = "__all__"


class AdDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='first_name',
        read_only=True,
    )

    class Meta:
        model = Ad
        fields = ["id", "name", "author_id", "author", "price", "description",
                  "is_published", "category_id", "image"]


class AdCreateSerializer(serializers.ModelSerializer):
    is_published = serializers.BooleanField(validators=[NotTrueValidator()])

    # id = serializers.IntegerField(required=False)
    # image = serializers.ImageField(required=False)
    #
    # author = serializers.SlugRelatedField(
    #     required=False,
    #     queryset=User.objects.all(),
    #     slug_field='username'
    # )
    # category = serializers.SlugRelatedField(
    #     required=False,
    #     queryset=Category.objects.all(),
    #     slug_field='name'
    # )

    class Meta:
        model = Ad
        fields = '__all__'
    #
    # def is_valid(self, raise_exception=False):
    #     self._author_id = self.initial_data.pop('author_id')
    #     self._category_id = self.initial_data.pop('category_id')
    #
    #     return super().is_valid(raise_exception=raise_exception)
    #
    # def create(self, validated_data):
    #     ad = Ad.objects.create(
    #         name=validated_data.get('name'),
    #         price=validated_data.get('price'),
    #         description=validated_data.get('description'),
    #         is_published=validated_data.get('is_published')
    #     )
    #     ad.author = get_object_or_404(User, pk=self._author_id)
    #     ad.category = get_object_or_404(Category, pk=self._category_id)
    #     ad.save()
    #     return ad


class AdUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(required=False)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Ad
        fields = "__all__"


class AdImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    is_published = serializers.BooleanField(read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'


class SelectionCreateSerializer(serializers.ModelSerializer):
    owner = SlugRelatedField(slug_field='username',
                             queryset=User.objects.all())

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionUpdateSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Selection
        fields = '__all__'
