from rest_framework import serializers
from serendipity.models import Section_info
from serendipity.models import Course

class SerendipitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields={'min_credits',
                'max_credits',
                'course_desc',
                'course_title',
                'course_prefix',
                'course_code'}