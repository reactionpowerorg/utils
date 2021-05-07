from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Responses(models.Model):
    CHOICES = [('1', 1),
               ('2', 2),
               ('3', 3),
               ('4', 4),
               ('5', 5), ]
    morale = models.IntegerField(max_length=1, null=True)
    top_goal = models.CharField(max_length=200, null=True)
    highlights = models.CharField(max_length=200, null=True)
    lowlights = models.CharField(max_length=200, null=True)
    w_load = models.CharField(max_length=500, null=True)
    goal_obs = models.CharField(max_length=100, null=True)
    m_tip = models.CharField(max_length=500, null=True)
    date = models.DateTimeField(auto_now=True,null=False)
    employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Surname = models.CharField(max_length=120, null=True)
    FirstName = models.CharField(max_length=120, null=True)
    LastName = models.CharField(max_length=120, null=True)
    Role = models.CharField(max_length=20, null=True)
    Gender = models.CharField(max_length=10, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
    ])
    ProfilePic = models.ImageField(upload_to="ProilePics/", blank=True, null=True)

    # def __str__(self):
    #     return self.user


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
