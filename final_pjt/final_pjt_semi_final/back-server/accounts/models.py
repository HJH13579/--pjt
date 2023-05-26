from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass
#이것만으로도 유저에 필요한 모든 필드 가져올 수 있음