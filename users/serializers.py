from rest_framework import serializers
from users.models import User, Location


class UserListSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username',
                  'role', 'age', 'locations']


class UserDetailSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username',
                  'role', 'age', 'locations']


class UserCreateSerializer(serializers.ModelSerializer):

    locations = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop('locations', [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        pas = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(pas)
        user.save()
        for location in self._locations:
            location_obj, _ = Location.objects.get_or_create(name=location)
            user.locations.add(location_obj)
        return user

    class Meta:
        model = User
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        many=True,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop('locations', [])
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        for locations in self._locations:
            location_obj, _ = Location.objects.get_or_create(name=locations)
            user.locations.add(location_obj)

        return user


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
