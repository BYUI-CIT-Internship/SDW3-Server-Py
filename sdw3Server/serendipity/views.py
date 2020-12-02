from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from serendipity.models import Semester
from serendipity.models import Course
from serendipity.serializers import SerendipitySerializer
from rest_framework.decorators import api_view


# Create your views here.
#First view to test just return all courses in the database
@api_view
def course_list(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            courses = courses.filter(title__icontains=title)
        
        serendipity_serializer = SerendipitySerializer(courses, many=True)
        return JsonResponse(serendipity_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
