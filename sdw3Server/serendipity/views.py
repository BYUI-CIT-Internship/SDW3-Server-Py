from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from serendipity.models import Semester
from serendipity.models import Course
from serendipity.serializers import SerendipitySerializer



# Create your views here.
#First view to test just return all courses in the database
@api_view(['GET'])
def course_list(request):
    if request.method == 'GET':
        serendipity_serializer = SerendipitySerializer(courses, many=True)
        return JsonResponse(serendipity_serializer.data, safe=False)
        # 'safe=False' for objects serialization