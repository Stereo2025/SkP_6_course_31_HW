from rest_framework import serializers


def not_published(value):
    if value:
        raise serializers.ValidationError(f"Значение поля is_published,"
                                          f" при создании объявления не"
                                          f" может быть True")
