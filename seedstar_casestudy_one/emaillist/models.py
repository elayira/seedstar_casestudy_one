from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class EmailList(models.Model):
    name = models.CharField(_("Email Holder's Name"), blank=False, max_length=255)
    email = models.EmailField(_("Email Address"), blank=False, unique=True)

