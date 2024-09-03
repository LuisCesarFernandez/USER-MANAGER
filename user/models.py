from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.
class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, null=False, unique=True)
    email = models.CharField(max_length=100, null=False, unique=True)
    password_hash = models.CharField(max_length=255, null=False)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=100, null=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'

    def set_password(self, raw_password):
        self.password_hash = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password_hash)

class Profile(models.Model):
    id_profile = models.AutoField(primary_key=True)
    bio = models.TextField()
    profile_picture_url = models.CharField(max_length=255, null=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'profile'

class Token(models.Model):
    id_token = models.AutoField(primary_key=True)
    token = models.CharField(max_length=500, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'token'