from django.db import models
from shop.models import MyUser
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    position = models.IntegerField()

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title


class Post(models.Model):
    STATUS_CHOICES = (
        ('p', 'publish'),
        ('d', 'draft')
    )
    title = models.CharField(max_length=20)
    slug = models.CharField(max_length=20)
    desc = models.TextField()
    category = models.ManyToManyField(Category , related_name="post")
    image = models.ImageField(upload_to='image/')
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)


class Course(models.Model):
    admin_id = models.ForeignKey(MyUser , on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser , on_delete=models.CASCADE)

