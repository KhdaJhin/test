from rest_framework.response import Response
from django import views
from api import models
from api.serializers import course as api_serializers
from rest_framework.views import APIView
from api.utils.response import BaseResponse
# 版本号
from rest_framework.versioning import URLPathVersioning
# Create your views here.
# a.查看所有学位课并打印学位课名称以及授课老师
class DegreeCourse(APIView):
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            all_degreecourse = models.DegreeCourse.objects.all()
            ser_obj=api_serializers.DegreeCourseSerializer(all_degreecourse,many=True)
            ret.data = ser_obj.data
        except Exception as  e:
            ret.code = 500
            ret.error = '获取数据失败！'
        return Response(ret.dict)
# b.查看所有学位课并打印学位课名称以及学位课的奖学金
class DegreeCourseScholarshipView(APIView):
    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            all_degreecourse = models.DegreeCourse.objects.all()
            print(11)
            ser_obj = api_serializers.DegreeCourseScholarshipSerializer(all_degreecourse, many=True)
            ret.data = ser_obj.data
        except Exception as  e:
            ret.code = 500
            ret.error = '获取数据失败！'
        return Response(ret.dict)
# #c.展示所有的专题课
class CourseView(APIView):
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            all_course = models.Course.objects.filter(degree_course__isnull=True).all()
            ser_obj=api_serializers.CourseSerializer(all_course,many=True)
            ret.data=ser_obj.data
        except Exception as  e:
            ret.code = 500
            ret.error='获取数据失败！'
        return Response(ret.dict)
# 课程详情api
class CourseDetailView(APIView):
    def get(self,request,pk,*args,**kwargs):
        ret = BaseResponse()
        # try:
        all_coursedetail = models.Course.objects.get(id=pk)
        ser_obj=api_serializers.CourseModelSerializer(instance=all_coursedetail)
        ret.data=ser_obj.data
        # except Exception as e :
        #     ret.code=500
        #     ret.error='获取数据失败！'
        return Response(ret.dict)


# d. 查看id=1的学位课对应的所有模块名称

# e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses

# f.获取id = 1的专题课，并打印该课程相关的所有常见问题

# g.获取id = 1的专题课，并打印该课程相关的课程大纲

# h.获取id = 1的专题课，并打印该课程相关的所有章节