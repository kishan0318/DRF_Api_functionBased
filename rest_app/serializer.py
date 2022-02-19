from django.db.models import fields
from rest_framework import serializers
from .models import Items

class ItemSerl(serializers.ModelSerializer):
    class Meta:
        model=Items
        fields=('__all__')
