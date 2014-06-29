from django.db import models
from django.utils.translation import ugettext as _
from developer.models import Developer

# Create your models here.

class File(models.Model):
    filename = models.CharField(max_length=250)
    path = models.CharField(max_length=350)
    folder = models.CharField(max_length=350)
    md5 = models.CharField(max_length=32)
    filetype = models.CharField(max_length=8)
    description = models.TextField()
    is_flashable = models.BooleanField(default=False)
    modified = models.CharField(max_length=35)
    status = models.SmallIntegerField(default=1)
    additional_info = models.TextField()
    short_url = models.CharField(max_length=32)
    developer = models.ForeignKey(Developer, null=True, blank=True, related_name="files")
    ro_developerid = models.CharField(max_length=50, blank=True)
    ro_board = models.CharField(max_length=50, blank=True)
    ro_rom = models.CharField(max_length=65, blank=True)
    ro_version = models.IntegerField(null=True, blank=True)
    gapps_package = models.IntegerField()
    incremental_file = models.IntegerField(null=True, blank=True)
    filesize = models.BigIntegerField()
    download_count = models.PositiveIntegerField(default=0)
    last_download = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('File')
        verbose_name_plural = _('Files')
        unique_together = ("path", "filename")


    def __unicode__(self):
        return u'%s' % self.path

class BlacklistKeyword(models.Model):
    keyword = models.CharField(max_length=150)
    status = models.BooleanField()

    class Meta:
        verbose_name = ('Blacklist Keyword')
        verbose_name_plural = _('Blacklist Keywords')

    def __unicode__(self):
        return u'%s' % self.keyword

