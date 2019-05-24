from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# USER PROFILE
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return str(self.user.username)

#Define SIGNALS so our User_Profile model will be automatically created/updated when User instances are.		
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()