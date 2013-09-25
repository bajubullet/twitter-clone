from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
  content = models.CharField(_('content'), max_length=140)
  author = models.ForeignKey(settings.AUTH_USER_MODEL)
  photo = models.ImageField(_('photo'),
                            upload_to='postphotos', null=True, blank=True)
  timestamp = models.DateTimeField(_('timestamp'), auto_now_add=True)
