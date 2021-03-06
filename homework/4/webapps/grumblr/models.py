from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length=42)
    user = models.ForeignKey(User)
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.post

class Profile(models.Model):
    age = models.PositiveSmallIntegerField()
    bio = models.CharField(max_length=420, default="Write your short bio here.", blank=True)
    user = models.OneToOneField(User, primary_key=True)
    picture = models.ImageField(upload_to="profile_pictures", blank=True)
    followees = models.ManyToManyField(
        User,
        related_name='User+',
    )

    @staticmethod
    def get_profile(user):
        try:
            profile = Profile.objects.get(user=user)
        except ObjectDoesNotExist:
            print('The profile does not exist.')

        return profile
