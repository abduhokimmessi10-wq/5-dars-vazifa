from rest_framework import serializers
from .models import Student, Course, Enrollment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'email', 'phone']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'duration']

class EnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    course_title = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = ['id', 'student_name', 'course_title', 'status', 'enrolled_at']

    def get_student_name(self, obj):
        return obj.student.full_name

    def get_course_title(self, obj):
        return obj.course.title