from django.conf.urls import url 
from serendipity import views 
 
urlpatterns = [ 
    url(r'^api/serendipity/courses$', views.course_list),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/tutorials/published$', views.tutorial_list_published)
]