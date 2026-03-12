from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=255,unique=True)
    phone = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Course(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    student_s = models.ManyToManyField(Student)


    def __str__(self):
        return self.title


from django.db import models


class Enrollment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='active')


    def __str__(self):
        return f"{self.student.full_name} - {self.course.title}"
