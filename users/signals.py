from django.db.models.signals import post_save
from django.contrib.auth.models import User # is the signal sender which will send
from django.dispatch import receiver 
from .models import profile
from library.models import issuedbooks , books # is the signal sender which will send

from library.models import issuebookhistory

# this runs when user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
     instance.profile.save()

'''
@receiver(post_save, sender=issuedbooks)
def create_issuebook_history(sender, instance, created, **kwargs):
    if created:
        issuebookhistory.objects.create(booksid=instance)


@receiver(post_save, sender=issuedbooks)
def save_issuebook_history(sender, instance, **kwargs):
    instance.issuebookhistory.save()
'''
