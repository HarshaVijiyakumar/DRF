from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, BaseUserManager
# Create your models here.
# basic_api/models.py


# Grade = [
#     ('excellent', 1),
#     ('average', 0),
#     ('bad', -1)
# ]
#
#
# # DataFlair
# class DRFPost(models.Model):
#     name = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)
#     uploaded = models.DateTimeField(auto_now_add= True)
#     rating = models.CharField(choices=Grade, default = 'average', max_length=50)
#
#     class Meta:
#         ordering = ['uploaded']
#
#     def __str__(self):
#         return self.name


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


# class UserProfile(AbstractBaseUser, PermissionsMixin):

class user_profile(AbstractBaseUser, PermissionsMixin):

    """Database model for user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_activate = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Return short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email


# Create your models here.
