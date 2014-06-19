from django.forms import widgets
from rest_framework import serializers
from files.models import SearchIndex

class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchIndex
