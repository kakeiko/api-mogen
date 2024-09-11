from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    pessoa = models.ForeignKey(to= User, on_delete=models.CASCADE, null=False, blank=False, related_name="pessoa")
    renda_mensal = models.FloatField(blank=False, null=False, max_length=20)

    def __str__(self):
        return str(self.pessoa.get_username)