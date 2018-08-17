import json
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response
from api import models
from api.serializers import course as api_serializers
from api.utils.response import BaseResponse


class CoursesView(ViewSetMixin,APIView):
    SHOPPING_CAR = {'1':{}}
    def list(self,request,*args,**kwargs):
        # response = {'code':1000,'data':None,'error':None}
        ret = BaseResponse()
        try:
            all_course = models.Course.objects.filter(degree_course__isnull=True).all()
            ser_obj = api_serializers.CourseModelSerializer(all_course, many=True)
            ret.data = ser_obj.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'

        return Response(ret.dict)
    # 用户将课程加入购物车
    def create(self,request,*args,**kwargs):
        """
        增加
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # 接收后端发送的数据
        ret=json.loads(request.body.decode('utf8'))
        # 课程id
        id=ret['1']['course_id']
        # 课程名称
        course_name=ret['1']['course_name']
        # 价格策略
        valid_period=ret['1']['end_price']
        # 课程价格
        course_price=ret['1']['course_price']
        # 先找到此课程
        verify_course=models.Course.objects.filter(id=id).first()
        # 如果存在
        if verify_course:
            # 找价格策略
            ser_obj = api_serializers.PricepolicySerializer(verify_course)
            # 如果存在
            if  valid_period in  ser_obj.data['pricepolicy'][0]:
                # 写入购物车
                self.SHOPPING_CAR['1'][id]= {'title':course_name,'price':course_price,'price_list':ser_obj.data['pricepolicy'][1]}
                # 打印购物车内容
                print(self.SHOPPING_CAR)
                # 成功返回数据
                return Response('加入购物车成功')
            else:
                # 价格策略失败返回数据
                return Response('不存在此价格策略')
        #     不存在课程返回数据
        return Response('不存在这个课程')

    def retrieve(self, request, pk, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            course = models.Course.objects.get(id=pk)
            ser = api_serializers.CourseModelSerializer(instance=course)
            response['data'] = ser.data
        except Exception as e:
            response['code'] = 500
            response['error'] = '获取数据失败'
        return Response(response)

    def update(self,request, pk, *args, **kwargs):
        """
        修改
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def destroy(self, request, pk, *args, **kwargs):
        """
        删除
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """