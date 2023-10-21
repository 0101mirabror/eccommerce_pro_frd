from django.db import models
from django.contrib.auth.models  import AbstractUser

 


class CustomUser(AbstractUser):
   email = models.EmailField(unique=True)
   username = models.CharField(max_length=20, unique=True)
   firstname = models.CharField(max_length=20)
   lastname = models.CharField(max_length=20)
#    custom_groups = models.ManyToManyField(Group, related_name='custom_users')
#    user_permissions = models.ManyToManyField(Permission, related_name='custom_users', related_query_name='custom_user')
#    image = models.ImageField(upload_to="media/profile_pictures", default="author_images/profile.png",null=True, blank=True)



