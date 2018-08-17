from django.shortcuts import render,HttpResponse
from rest_framework import serializers
# Create your views here.
from api import models
def ceshi(request):
# a.查看所有学位课并打印学位课名称以及授课老师
    object=models.DegreeCourse.objects.values_list('name','teachers__name')
    print(object)

# b.查看所有学位课并打印学位课名称以及学位课的奖学金
#     object=models.DegreeCourse.objects.values_list('name','scholarship__value')
#     print(object)

# c.展示所有的专题课
# models.Course.objects.filter(degree_course__isnull=True)
#     object=models.Course.objects.filter(degree_course__isnull=True).all()
#     print(object)

# d.查看id = 1
# 的学位课对应的所有模块名称
#     object = models.DegreeCourse.objects.filter(id=1).values('course__name')
#     print(object)

# e.获取id = 1
# 的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses //source='get_type_display'
#     object1=models.Course.objects.filter(degree_course__isnull=True,id=1).values('name','coursedetail__why_study','coursedetail__what_to_study_brief','coursedetail__recommend_courses')
#     object= models.Course.objects.filter(degree_course__isnull=True, id=1).all()
# #     打印等级
#     for i in object:
#         print(i.get_level_display())
#     # 打印除了等级的所有信息
#     print(object1)
# f.获取id = 1
# 的专题课，并打印该课程相关的所有常见问题
#     object = models.OftenAskedQuestion.objects.filter(object_id=1).values('question')
#     print(object)

# g.获取id = 1
# 的专题课，并打印该课程相关的课程大纲
#     object = models.Course.objects.filter(degree_course__isnull=True,id=1).values('coursedetail__courseoutline__content')
#     print(object)

# h.获取id = 1
# 的专题课，并打印该课程相关的所有章节
#     object = models.Course.objects.filter(degree_course__isnull=True, id=1).values('coursechapters__name')
#     print(object)

# i.获取id = 1
# 的专题课，并打印该课程相关的所有课时
#     obj = models.Course.objects.get(id=1)
#     chapter_list = obj.coursechapters.all()
#     for chapter in chapter_list:
#         print(chapter.name)
#         for item in chapter.coursesections.all():
#             print(item)
    # section_list1 = models.CourseSection.objects.filter(chapter__course_id=1).all()
    # section_list = models.CourseSection.objects.filter(chapter__course_id=1).values('id','name','chapter_id','chapter__name')
    # print(section_list)
    # for item in section_list:
    #     print(item)
    # object = models.Course.objects.filter(degree_course__isnull=True, id=1).values('coursechapters__name','coursechapters__coursesections__name')

    # print(object)
# 第1章·Python
# 介绍、基础语法、流程控制
# 01 - 课程介绍（一）
# 01 - 课程介绍（一）
# 01 - 课程介绍（一）
# 01 - 课程介绍（一）
# 01 - 课程介绍（一）
# 第1章·Python
# 介绍、基础语法、流程控制
# 01 - 课程介绍（一）
# 01 - 课程介绍（一）
# 01 - 课程介绍（一）
# 01 - 课程介绍（一）
# 01 - 课程介绍（一）
# i.获取id = 1
# 的专题课，并打印该课程相关的所有的价格策略
#     object = models.PricePolicy.objects.filter(object_id=1).all()
#     print(object)
    return HttpResponse('ok')