from django.conf.urls import url
from api.views import course


urlpatterns = [
    url(r'course/$',course.CoursesView.as_view({'get':'list','post':'create'})),
    url(r'course/(?P<pk>\d+)/$',course.CoursesView.as_view({'get':'retrieve','put':'update','delete':'destroy'}))
]