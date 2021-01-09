from django.db import models


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





