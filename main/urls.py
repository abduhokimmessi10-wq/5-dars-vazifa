from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentListAPIView,CourseDetailAPIView,EnrollmentListAPIView


router = DefaultRouter()
router.register('course', CourseDetailAPIView,basename='course')

urlpatterns = [
    path('student/', StudentListAPIView.as_view(), name='student-list'),
    path('enrollment/', EnrollmentListAPIView.as_view(), name='enrollment-list'),
    path('', include(router.urls)),
]