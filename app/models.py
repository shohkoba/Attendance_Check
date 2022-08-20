from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Child(models.Model):
    name = models.CharField(
        verbose_name='名前',
        max_length=100,
    )
    
    def __str__(self):
        return self.name


class Attendance(models.Model):
    date = models.DateField(
        verbose_name='日付',
        default=timezone.now,
    )
    
    child = models.ForeignKey(
        Child,
        on_delete = models.CASCADE,
        verbose_name = 'お子様の名前',
    )
    
    ATTEND_CHOICES = (
        (1, '出席'),
        (2, '欠席'),
    )
    attendance = models.IntegerField(
        verbose_name = '出欠',
        choices = ATTEND_CHOICES,
    )
    
    reason = models.TextField(
        verbose_name = '欠席理由',
        max_length = 1000,
        blank = True,
        null = True,
    )
    
    respon = models.TextField(
        verbose_name = '返信',
        max_length = 1000,
        blank = True,
        null = True,
    )