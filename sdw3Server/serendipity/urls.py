from django.conf.urls import url 
from serendipity import views 
 
urlpatterns = [ 
    url(r'^api/serendipity/courses$', views.course_list),
]