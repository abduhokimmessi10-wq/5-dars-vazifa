from django.shortcuts import render
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Student,Course,Enrollment
from .serializers import StudentSerializer,CourseSerializer,EnrollmentSerializer
from .permissions import IsAdminOrReadOnly

class StudentListAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseDetailAPIView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'duration', 'created_at']


class EnrollmentListAPIView(ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

    def get_queryset(self):
        return Enrollment.objects.select_related('student', 'course').all()


