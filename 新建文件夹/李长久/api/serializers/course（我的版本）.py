from api import models
from rest_framework import serializers
# 查看所有学位课并打印学位课名称以及授课老师的序列化
class DegreeCourseSerializer(serializers.ModelSerializer):
    teachers_name = serializers.SerializerMethodField()
    class Meta:
        model = models.DegreeCourse
        fields = ['name','teachers_name']
        depth=1
    def get_teachers_name(self,row):
        teachers = row.teachers.all()
        return [ {'id':item.id,'name':item.name} for item in teachers]
# 查看所有学位课并打印学位课名称以及学位课的奖学金的序列化
class DegreeCourseScholarshipSerializer(serializers.ModelSerializer):
    # 外键查询
    # 方法一：直接用scholarship_set
    scholarship_set = serializers.StringRelatedField(many=True)
    # 方法二：在models中给外键起个名字 这样直接找名字就可以
    # scholarship = serializers.SerializerMethodField()

    class Meta:

        model = models.DegreeCourse
        fields = ['name','scholarship_set']
        depth=1

    # def get_scholarship(self, row):
    #         recommend_list = row.degreecourse_name.all()
    #         return [{'id': item.id, 'value': item.value} for item in recommend_list]


# 专题课的序列化
class CourseSerializer(serializers.ModelSerializer):
    type_str = serializers.CharField(source='get_level_display', read_only=True)
    class Meta:
        model = models.Course
        fields = "__all__"

# class CourseDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.CourseDetail
#         fields = "__all__"
class CourseModelSerializer(serializers.ModelSerializer):
    # 查看等级中文
    level_name = serializers.CharField(source='get_level_display')
    # 显示具体时间
    hours = serializers.CharField(source='coursedetail.hours')
    # 为什么学习
    whystudy = serializers.CharField(source='coursedetail.why_study')
    # 学完之后能干什么
    what_to_study_brief = serializers.CharField(source='coursedetail.what_to_study_brief')
    # 标题
    course_slogan = serializers.CharField(source='coursedetail.course_slogan')
    # 推荐课程
    recommend_courses = serializers.SerializerMethodField()
    # 常见问题
    oftenaskedquestion = serializers.SerializerMethodField()
    # 课程大纲
    courseoutline=serializers.SerializerMethodField()
    #所有的章节
    coursechapter = serializers.SerializerMethodField()
    class Meta:
        model = models.Course
        fields = ['id','name','level_name','hours','course_slogan','recommend_courses','whystudy','what_to_study_brief','oftenaskedquestion','courseoutline','coursechapter']

    def get_recommend_courses(self,row):
        recommend_list = row.coursedetail.recommend_courses.all()
        return [ {'id':item.id,'name':item.name} for item in recommend_list]
    def get_oftenaskedquestion(self,row):
        oftenaskedquestion_list = row.asked_question.all()
        return [{'question':item.question,'answer':item.answer} for item in oftenaskedquestion_list]
    def get_courseoutline(self,row):
        courseoutline_list = row.coursedetail.courseoutline_set.all()
        return [{'content':item.content} for item in courseoutline_list]
    def get_coursechapter(self,row):
        coursechapter_list = row.coursechapters.all()
        return [{'name':item.name} for item in coursechapter_list]