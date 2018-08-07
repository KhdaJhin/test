from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from api import models
from api.serializers.course import CourseModelSerializer, CourseSerializers, DegreeCourseSerializers
from api.utils.response import BaseResponse
from django.shortcuts import render

class CoursesView(APIView):

    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            # 从数据库获取数据
            query_set = models.Course.objects.all()

            # 分页
            page = PageNumberPagination()
            course_list = page.paginate_queryset(query_set, request, self)

            # 分页后执行序列化
            ser = CourseModelSerializer(instance=course_list, many=True)

            # 展示所有专业课
            pro_cou = models.Course.objects.filter(degree_course__isnull=True)
            print(pro_cou)

            ret.data = ser.data
        except Exception as e:
            print(e)
            ret.get_error()
        return Response(ret.dict)


class CoursesDetailView(APIView):

    def get(self, request, pk, *args, **kwargs):
        ret = BaseResponse()
        try:
            course = models.Course.objects.get(id=pk)
            ser = CourseModelSerializer(instance=course)
            ret.data = ser.data
        except Exception as e:
            print(e)
            ret.get_error()
        return Response(ret.dict)


class DegreeCourseView(APIView):

    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            deg_cou = models.DegreeCourse.objects.all()

            # 查询id=1的学位课的所有模块名称
            deg_cou_1 = models.DegreeCourse.objects.get(id=1)
            temp = deg_cou_1.course_set.all()
            print(temp)

            ser = DegreeCourseSerializers(instance=deg_cou, many=True)
            print()
            ret.data = ser.data
        except Exception as e:
            ret.get_error()
        # 查看所有学位课并打印学位课名称以及授课老师
        for i in ret.dict['data']:
            print(f'学位课：{i["name"]}, 授课教师：{i["teachers"][0]}')
            # 打印奖学金额
            print(f'该门课程奖学金：{i["scholarship"]}')

        return Response(ret.dict)


class ShowOneCourseView(APIView):

    def get(self, request):
        ret = BaseResponse()
        try:
            # 获取id=1的专题课
            pro_cou_1 = models.Course.objects.filter(id=1)

            pass
        except Exception as e:
            print(e)
            pass


