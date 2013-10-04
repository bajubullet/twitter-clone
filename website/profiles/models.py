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

  @property
  def users_following(self):
    """
    Returns a list of IDs of users following.
    """
    following = self.following.all().values_list('followee')
    following = [user[0] for user in following]
    following.append(self.id)
    return following

  @property
  def photo_url(self):
    """
    Returns user photo url else default user pic url.
    """
    try:
      return self.photo.url
    except ValueError:
      return '/static/img/default_user.jpg'

