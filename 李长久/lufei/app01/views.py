from django.shortcuts import render
from api.models import *
# Create your views here.


def index(request):

    # 查看所有与学位课并打印学位课名称以及授课老师
    degree_list = DegreeCourse.objects.all()
    for degree in degree_list:
        print(degree.name)
        for tch in degree.teachers.all():
            print(tch.name)

    # 查看所有学位课并打印学位课名称以及学位课奖学金
    for deg in degree_list:
        print(deg.name, deg.total_scholarship)

    # 展示所有专题课
    thematic_course = Course.objects.filter(degree_course__isnull=True)

    # 查看id=1的学位课对应的所有模块名称
    model_1 = DegreeCourse.objects.filter(id=1).first()
    print(model_1.course_set.all().first().name)

    # 获取id=1的专题课，并打印：课程名、级别（中文）、why_study、what_to_study_brief、所有
    the_cou = Course.objects.filter()

    return render(request, 'index.html', {'thematic_course': thematic_course, 'tch': the_cou})
