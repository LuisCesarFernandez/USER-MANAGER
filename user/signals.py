from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            id_user = instance,
            bio = 'This is your bio for default.',
            profile_picture_url = 'https://as2.ftcdn.net/jpg/02/15/84/43/220_F_215844325_ttX9YiIIyeaR7Ne6EaLLjMAmy4GvPC69.jpg')