from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # Check if the user is a regular user (not superuser or staff)
    if not instance.is_superuser and not instance.is_staff:
        if created:
            # Create profile for new regular user
            Profile.objects.create(user=instance)
        else:
            # Try to save profile if the user exists
            try:
                instance.profile.save()
            except Profile.DoesNotExist:
                # Handle case where profile doesn't exist (just in case)
                Profile.objects.create(user=instance)