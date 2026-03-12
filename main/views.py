from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Student, Course, Enrollment
from .serializers import (
    StudentSerializer, CourseSerializer,
    EnrollmentSerializer, StudentSerializerForDetail
)
from rest_framework.pagination import CursorPagination


class StudentListAPIView(ModelViewSet):
    def get_serializer_class(self):
        if self.kwargs.get('pk'):
            return StudentSerializerForDetail
        return StudentSerializer

    def get_queryset(self):
        if self.kwargs.get('pk'):
            return Student.objects.prefetch_related('course_set').all()
        return Student.objects.all()


class MyPagination(CursorPagination):
    ordering = ['-pk']
    page_size = 2

class CourseDetailAPIView(ModelViewSet):
    # queryset = Course.objects.only(
    #     'id', 'title', 'description', 'price', 'duration'
    # ).prefetch_related('student_s')
    queryset = (Course.objects.defer('price')
                .prefetch_related('student_s'))
    serializer_class = CourseSerializer
    pagination_class = MyPagination

class EnrollmentListAPIView(ListCreateAPIView):
    serializer_class = EnrollmentSerializer

    def get_queryset(self):
        return Enrollment.objects.select_related('student', 'course').all()