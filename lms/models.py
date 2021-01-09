from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Day(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Time(models.Model):
    first_start = '07:30'
    second_start = '09:00'
    third_start = '10:30'
    forth_start = '14:00'
    fifth_start = '16:00'
    starts = {
        (first_start, '07:30'), (second_start, '09:00'), (third_start, '10:30'),
        (forth_start, '14:00'), (fifth_start, '16:00')
    }
    first_end = '09:00'
    second_end = '10:30'
    third_end = '12:00'
    forth_end = '15:30'
    fifth_end = '17:30'
    ends = {
        (first_end, '09:00'), (second_end, '10:30'), (third_end, '12:00'),
        (forth_end, '15:30'), (fifth_end, '17:30')
    }
    start_time = models.CharField(max_length=5, choices=starts, default=first_start)
    end_time = models.CharField(max_length=5, choices=ends, default=first_end)

    def __str__(self):
        return str(self.start_time) + ' - ' + str(self.end_time)


class Faculty(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Faculties"

    def __str__(self):
        return self.name


class Room(models.Model):
    room_number = models.IntegerField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.room_number) + ' ' + str(self.faculty)


class Location(models.Model):
    date = models.ForeignKey(Day, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.room) + ' : ' + str(self.date) + ' ' + str(self.time)


class Professor(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    mail = models.EmailField(max_length=100, null=True)
    website = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)


class Student(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    student_number = models.CharField(max_length=9, null=False, unique=True)
    full_name = str(first_name) + ' ' + str(last_name)

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)


class Course(models.Model):
    name = models.CharField(max_length=20, null=False)
    location = models.OneToOneField(Location, unique=True, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student,
                                      through='StudentCourse',
                                      through_fields=('course', 'student'))
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + ' (' + str(self.professor) + ') : ' + str(self.location)


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.FloatField(null=False, validators=[MinValueValidator(20.0), MaxValueValidator(0)],)

    def __str__(self):
        return str(self.student) + ' (' + str(self.course.name) + ') : ' + str(self.grade)





