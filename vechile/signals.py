from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from django.core.cache import cache


@receiver(post_save)
def make_post_save(sender, instance, created, **kwargs):
    if created:
        instances = Make.objects.all().order_by('-created_at')
        cache.set('make_cache', instances)


@receiver(post_save)
def vechile_post_save(sender, instance, created, **kwargs):
    if created:
        instances = Vechile.objects.all().order_by('-created_at')
        cache.set('vechile_cache', instances)
