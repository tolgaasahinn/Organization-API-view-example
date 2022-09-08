from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    class Meta:
        db_table = "user"
        verbose_name_plural = "Users"
        verbose_name = "Users"

    def __str__(self) -> str:
        return self.username
