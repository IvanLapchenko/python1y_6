from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class BaseModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        abstract = True


class Question(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
