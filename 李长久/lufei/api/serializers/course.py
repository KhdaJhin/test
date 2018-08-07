from rest_framework import serializers
from api import models


class CourseSerializers(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()

    def clear(self):
        return self.name


class CourseModelSerializer(serializers.ModelSerializer):

    level_name = serializers.CharField(source='get_level_display')
    hours = serializers.CharField(source='coursedetail.hours')
    course_slogan = serializers.CharField(source='coursedetail.course_slogan')
    why_std = serializers.CharField(source='coursedetail.why_study')
    study_todo = serializers.CharField(source='coursedetail.what_to_study_brief')
    cou_question = serializers.SerializerMethodField()      # CharField(source='asked_question.question')
    # recommend_courses = serializers.CharField(source='coursedetail.recommend_courses.all')

    recommend_courses = serializers.SerializerMethodField()
    professional_courses = serializers.SerializerMethodField()
    outline = serializers.SerializerMethodField()
    # all_chapters = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = [
            'id', 'name', 'level_name', 'hours',
            'course_slogan', 'recommend_courses', 'professional_courses',
            'why_std', 'study_todo', 'study_todo', 'cou_question',
            'outline',
            # 'all_chapters'
        ]

    def get_recommend_courses(self, row):
        recommend_list = row.coursedetail.recommend_courses.all()
        return [{'id': i.id, 'name': i.name} for i in recommend_list]

    def get_professional_courses(self, cou):
        pro_list = models.Course.objects.filter(degree_course__isnull=True)
        return [i.name for i in pro_list]

    def get_cou_question(self, cou):
        cou_que_list = cou.asked_question.all()
        return [i.question for i in cou_que_list]

    def get_outline(self, cou):
        outlin_list = cou.coursedetail.courseoutline_set.all()
        return [i.content for i in outlin_list]

    # def get_all_chapters(self, cou):
    #     cha_list = cou.coursechapters.all()
    #     return [{'chapter': i} for i in cha_list]


class DegreeCourseSerializers(serializers.ModelSerializer):

    teachers = serializers.SerializerMethodField()
    scholarship = serializers.SerializerMethodField()

    class Meta:
        model = models.DegreeCourse
        fields = [
            'name', 'teachers', 'scholarship',
        ]

    def get_teachers(self, dc):
        tch_list = dc.teachers.all()
        return [tch.name for tch in tch_list]

    def get_scholarship(self, dc):
        dc_li = dc.scholarship_set.all()
        print(dc_li)
        return [i.value for i in dc_li]


class ProfessionalCourseSerializer(serializers.ModelSerializer):

    # cou_

    class Meta:
        model = models.Course
        fields = [
            ''
        ]
