from django.contrib.auth.models import Group, Permission
from django.db import models
from django.contrib.auth.models import AbstractUser
class Z119group(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class CustomUser(AbstractUser):
    z119group = models.ForeignKey(Z119group, on_delete=models.SET_NULL, null=True, blank=True)
    is_leader = models.BooleanField(default=False)
    group_name = models.CharField(max_length=100, blank=True, null=True)
    is_director = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
class WorkerInfo(models.Model):
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    z119group = models.ForeignKey(Z119group, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    def __str__(self):
        return self.name
class AttendanceRecord(models.Model):
    worker = models.ForeignKey(WorkerInfo, on_delete=models.CASCADE)
    date = models.DateField()
    report_time = models.DateTimeField(null=True, blank = True)
    status = models.CharField(max_length=100, choices=[
        ('present', 'Đi làm theo SP'),
        ('presenttg','Đi làm theo thời gian'),
        ('curve','Đi công tác'),
        ('absent', 'Nghỉ đột xuất'),
        ('leave', 'Nghỉ phép'),
        ('gostation', 'Đi gác'),
        ('pregnancy','ốm đau, thai sản'),
        ('study','Đi học'),
        ('studynuangayinZ','Học nửa ngày ở Nhà máy'),
        ('studyfullinZ','Học cả ngày ở Nhà máy'),
        ('nghichohuu','Nghỉ chờ hưu'),
        ('kinhte','Kinh tế'),
    ])
    note = models.TextField(blank=True, null=True)
    report_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        unique_together = ('worker', 'date')
    def __str__(self):
        return f"{self.worker.name} - {self.date} - {self.status}"
