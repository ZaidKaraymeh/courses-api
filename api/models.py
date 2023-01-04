from django.db import models
import uuid
# Create your models here.


class Course(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    instructor = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    sections = models.ManyToManyField("api.Section")
    
    title = models.CharField(max_length=155)
    thumbnail = models.FileField(upload_to='thumbnail', max_length=100)
    description = models.TextField(max_length=9000)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)


class Section(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    lectures = models.ManyToManyField("api.Lecture")
    
    title = models.CharField(max_length=155)
    thumbnail = models.FileField(upload_to='thumbnail', max_length=100)
    description = models.TextField(max_length=9000)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

class Lecture(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    title = models.CharField(max_length=155)
    thumbnail = models.FileField(upload_to='thumbnails', max_length=100)
    lecture = models.FileField(upload_to='lectures', max_length=100)

    description = models.TextField(max_length=9000)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)