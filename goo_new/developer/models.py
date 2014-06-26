from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class Developer(models.Model):
    developer_path = models.CharField(max_length=450)
    username = models.CharField(max_length=100)
    avatar = models.CharField(max_length=250)
    avatar_thumb = models.CharField(max_length=50)
    alias = models.CharField(max_length=150)
    releases = models.TextField()
    services = models.CharField(max_length=250)
    referral = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    denied = models.BooleanField(default=False)
    bio = models.TextField()
    foldername = models.CharField(max_length=250, default="")
    twitter = models.CharField(max_length=300)
    rootzwiki = models.CharField(max_length=300)
    xda = models.CharField(max_length=300)
    googleplus = models.CharField(max_length=350)
    email = models.CharField(max_length=250)
    xda_rd_url = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Developer')
        verbose_name_plural = _('Developers')

    def __unicode__(self):
        return u'%s' % self.username	
