from rest_framework import serializers
from .models import Student, Course, Enrollment


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'email', 'phone']


class CourseSerializerForStudent(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'duration']


class StudentSerializerForDetail(serializers.ModelSerializer):
    courses = CourseSerializerForStudent(source='course_set', read_only=True, many=True)

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'email', 'phone', 'courses']


class CourseSerializer(serializers.ModelSerializer):
    students = StudentSerializer(source='student_s', read_only=True, many=True)
    student_ids = serializers.PrimaryKeyRelatedField(
        source='student_s',
        queryset=Student.objects.all(),
        many=True,
        write_only=True
    )

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'duration', 'students', 'student_ids']


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