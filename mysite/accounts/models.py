
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User,unique=True, null=False, db_index=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Product(models.Model):
	prod_id = models.OneToOneField(User,unique=True, null=False, db_index=True)
	name = models.CharField(max_length=300)
	slug = models.SlugField(max_length=150)
	description = models.TextField()
	photo = models.ImageField(upload_to='product_photo',
	blank=True)
	price_in_dollars = models.DecimalField(max_digits=6,
	decimal_places=2)