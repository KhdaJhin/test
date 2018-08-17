from rest_framework.response import Response
from django import views
from api import models
from api import serializers as api_serializers
from rest_framework.views import APIView
# Create your views here.
#查询学位课
class DegreeCourse(APIView):
    def get(self,request):
        res={'code':0}
        all_degreecourse = models.DegreeCourse.objects.all()
        ser_obj=api_serializers.DegreeCourseSerializer(all_degreecourse,many=True)
        res["data"] = ser_obj.data
        return Response(res)
# 查询专题课
class Course(APIView):
    def get(self,request):
        res={'code':0}
        all_course = models.Course.objects.filter(degree_course__isnull=True).all()
        ser_obj=api_serializers.CourseSerializer(all_course,many=True)
        res["data"] = ser_obj.data
        return Response(res)
# 查询课程详情
class CourseDetail(APIView):
    def get(self,request):
        res={'code':0}
        all_coursedetail = models.CourseDetail.objects.all()
        ser_obj=api_serializers.CourseDetailSerializer(all_coursedetail,many=True)
        res["data"] = ser_obj.data
        return Response(res)