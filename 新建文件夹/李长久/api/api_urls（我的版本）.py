from django.conf.urls import url
from api.views import course

urlpatterns = [
    # a.查看所有学位课并打印学位课名称以及授课老师
    url(r'degreecourse/', course.DegreeCourse.as_view()),
    url(r'degreecoursescholarship/', course.DegreeCourseScholarshipView.as_view()),
    # 查看专题课的api
    url(r'course/', course.CourseView.as_view()),
    # 查看专题课详情的api
    url(r'coursedetail/(?P<pk>\d+)', course.CourseDetailView.as_view()),
]