from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Argument(models.Model):
    title = models.CharField(max_length=200)
    topic = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Vote(models.Model):
    VOTE_CHOICES = (
        ('up', 'Upvote'),
        ('down', 'Downvote'),
    )
    argument = models.ForeignKey(Argument, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=4, choices=VOTE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('argument', 'user')

    def __str__(self):
        return f"{self.user} - {self.argument} - {self.vote_type}"

# Create your models here.
