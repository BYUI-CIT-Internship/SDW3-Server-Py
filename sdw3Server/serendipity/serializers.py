from rest_framework import serializers
import serendipity.models

class SerendipitySerializer(serializers.ModelSerializer):
    class Meta:
        model = modelname
        fields=