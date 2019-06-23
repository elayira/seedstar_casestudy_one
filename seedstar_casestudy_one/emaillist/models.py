from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Email(models.Model):
    email = models.EmailField(blank=False, unique=True)


class EmailName(models.Model):
    name = models.CharField(_("Name of email"), blank=False, max_length=255)
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
