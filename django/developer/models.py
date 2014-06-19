from django.db import models

# Create your models here.

class Developer(models.Model):
	developer_path = models.CharField(max_length=450)
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=200)
	avatar = models.CharField(max_length=250)
	avatar_thumb = models.CharField(, max_length=50)
	bio = models.TextField()
	twitter = models.CharField(max_length=300)
	rootzwiki = models.CharField(max_length=300)
	xda = models.CharField(max_length=300)
	googleplus = models.CharField(max_length=350)
	email = models.CharField(max_length=250)
	xda_rd_url = models.CharField(, max_length=50)
	created = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField()
    
    class Meta:
        verbose_name = _('Developer')
        verbose_name_plural = _('Developers')

    def __unicode__(self):
        return u'%s' % self.username


class Application(models.Model):
	alias = models.CharField(max_length=150)
	email = models.CharField(max_length=150)
	twitter = models.CharField(max_length=250)
	googleplus = models.CharField(max_length=350)
	xda = models.CharField(max_length=350)
	bio = models.TextField()
	releases = models.TextField()
	username = models.CharField(max_length=250)
	foldername = models.CharField(max_length=250)
	services = models.CharField(max_length=250)
	referral = models.CharField(max_length=250)
	timestamp = models.DateTimeField(auto_now_add=True)
	processed = models.BooleanField()
	denied = models.BooleanField()

        class Meta:
            verbose_name = _('Application')
 
            verbose_name_plural = _('Applications')

    
        def __unicode__(self):
            return u'%s' % self.alias


    
            