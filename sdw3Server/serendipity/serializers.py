from rest_framework import serializers
from serendipity.models import Section_info

class SerendipitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Section_info
        fields={
        }