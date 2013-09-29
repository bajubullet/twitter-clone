from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class SiteUser(AbstractUser):
  MALE = 'M'
  FEMALE = 'F'
  GENDER_CHOICES = (
      (MALE, _('Male')),
      (FEMALE, _('Female')),
  )
  bio = models.CharField(_('bio'), max_length=200, null=True, blank=True)
  gender = models.CharField(_('gender'), max_length=1, choices=GENDER_CHOICES)
  photo = models.ImageField(_('photo'),
                            upload_to='profilephotos', null=True, blank=True)
  website = models.URLField(_('website'), null=True, blank=True)
