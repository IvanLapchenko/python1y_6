from django.contrib.postgres.fields import ArrayField
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
    up_votes = ArrayField(models.IntegerField(default=0), default=list)
    down_votes = ArrayField(models.IntegerField(default=0), default=list)

    def upvote(self, user):
        if user not in self.up_votes:
            if user in self.down_votes:
                self.down_votes.remove(user)
            self.up_votes.append(user)
            self.save()
            # print(user)
            # print(f"{self.up_votes} - are upvotes")
            # print(f"{self.down_votes} - are downvotes")

    def downvote(self, user):
        if user not in self.down_votes:
            if user in self.up_votes:
                self.up_votes.remove(user)
            self.down_votes.append(user)
            self.save()
            # print(user)
            # print(f"{self.up_votes} - are upvotes")
            # print(f"{self.down_votes} - are downvotes")

    def get_rating(self):
        return len(self.up_votes) - len(self.down_votes)

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


class Notification(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    post_id = models.IntegerField()
    post_type = models.CharField()
    action = models.TextField()

    # def __init__(self, user, post_id, post_type, action, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.from_user = user
    #     self.post_id = post_id
    #     self.post_type = post_type
    #     self.action = action


