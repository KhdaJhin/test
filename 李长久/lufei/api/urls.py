from django.conf.urls import url
from api.views import course


urlpatterns = [
    url(r'course/$', course.CoursesView.as_view()),
    url(r'course/(?P<pk>\d+)/$', course.CoursesDetailView.as_view()),
    url(r'degree/course/$', course.DegreeCourseView.as_view()),
    url(r'show/professional1/$', course.ShowOneCourseView.as_view()),

]
