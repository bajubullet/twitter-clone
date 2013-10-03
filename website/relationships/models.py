from django.db import models


class Relationship(models.Model):
  followee = models.ForeignKey('profiles.SiteUser', related_name='followers')
  follower = models.ForeignKey('profiles.SiteUser', related_name='following')
  timestamp = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return '%s is following %s' % (
        self.follower.username, self.followee.username)
